from Client import *
import parameters as pr
from model_train import *
from Server import *
import load_data as ld
from tensorflow.keras import backend as K

def executeFL(client_lists, global_model, X_test, y_test, round):
    
    #create batched test data
    testBatched = pr.tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(32)

    #create batched clients data list
    clients_batched = ld.batched(client_lists)

    print(f'    START train at Round {round + 1}/{pr.num_rounds}')
    
    #create a list to store weights of each client
    client_weights = []
    
    # Train model with each client
    for (i, client) in enumerate(client_lists):
        client.model.set_weights(global_model.get_weights())  # update weights
        weights = train_on_client(client.model, clients_batched[i])  # Training
        client_weights.append((weights, len(client.data)))  # Store weight

    # Aggregating global weights
    global_weights = average_weights(client_weights)
    global_model.set_weights(global_weights)  # update global
    
    # Evaluate global model on test data
    total_loss = 0
    total_accuracy = 0
    num_batches = 0
    for features, labels in testBatched:
        loss, accuracy = global_model.evaluate(features, labels, verbose=0)
        total_loss += loss
        total_accuracy += accuracy
        num_batches += 1

    # Calculate average loss and accuracy
    avg_loss = total_loss / num_batches if num_batches > 0 else 0
    avg_accuracy = total_accuracy / num_batches if num_batches > 0 else 0

    print(f'    --END train at Round {round + 1}/{pr.num_rounds}--')
    return avg_loss, avg_accuracy, global_model


    

def examine_data_trained(clients, mode):
    total_data = 0

    if mode == 'FedCS':
        client_ids = [client.id for client in clients]
        print('Running FedCS with clients:', len(client_ids))
        # client_UD_time = [client.get_update_time(round) for client in clients]
        # print('Client update time:', client_UD_time)
        # client_UL_time = [client.get_upload_time(round) for client in clients]
        # print('Client upload time:', client_UL_time)
        total_data = sum([len(client.data) for client in clients])
        # print('Total data FedCS:', total_data)
        

    elif mode == 'DDr':
        client_ids = [client.id for client in clients]
        print('Running DDr with clients:', len(client_ids))
        # client_UD_time = [client.get_update_time(round) for client in clients]
        # print('Client update time:', client_UD_time)
        # client_UL_time = [client.get_upload_time(round) for client in clients]
        # print('Client upload time:', client_UL_time)
        total_data = sum([len(client.data) for client in clients])
        # print('Total data DDr:', total_data)
        # print("")

    return total_data

if __name__ == '__main__':
    executeFL()