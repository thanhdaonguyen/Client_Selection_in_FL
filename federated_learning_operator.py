from Client import *
import parameters as pr
from model_train import *
from Server import *
import load_data as ld
from tensorflow.keras import backend as K

def executeFL():
    X_train,X_test,y_train,y_test = ld.get_data()
    client_lists = Client.create_clients(X_train,y_train, pr.num_clients, 'clients')  # create clients with random data
    global_model = create_keras_model()
    testBatched = pr.tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(32)
    results = {}
    print("--------------------Start training -------------------------")
    for round_num in range(pr.num_rounds):
        testBatched = testBatched.shuffle(buffer_size=1000)
        clients_batched = ld.batched(X_test,y_test,client_lists)
        print(f'    START train at Round {round_num + 1}/{pr.num_rounds}')
        client_weights = []
        
        # Train model with each client
        for client in range(pr.num_clients):
            client_model = create_keras_model()  # create model for client
            client_model.set_weights(global_model.get_weights())  # update weights
            weights = train_on_client(client_model, clients_batched[client])  # Training
            client_weights.append(weights)  # Store weight

        # Global weights
        global_weights = average_weights(global_model.get_weights(), client_weights)
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

        results[round_num + 1] = (avg_loss, avg_accuracy)  # Lưu kết quả vào dictionary
        print(f'    --END train at Round {round_num + 1}/{pr.num_rounds}--')
    print("----------------------End training ------------------------------------")
    ld.saveResultsToFile(results, pr.results_file_path + '\\result.txt')

def run_learning_process(clients, round, mode):
    if mode == 'FedCS':
        client_ids = [client.id for client in clients]
        print('Running FedCS with clients:', len(client_ids))
        # client_UD_time = [client.get_update_time(round) for client in clients]
        # print('Client update time:', client_UD_time)
        # client_UL_time = [client.get_upload_time(round) for client in clients]
        # print('Client upload time:', client_UL_time)
        total_data = sum([client.data[round] for client in clients])
        print('Total data FedCS:', total_data)

    elif mode == 'DDr':
        client_ids = [client.id for client in clients]
        print('Running DDr with clients:', len(client_ids))
        # client_UD_time = [client.get_update_time(round) for client in clients]
        # print('Client update time:', client_UD_time)
        # client_UL_time = [client.get_upload_time(round) for client in clients]
        # print('Client upload time:', client_UL_time)
        total_data = sum([client.data[round] for client in clients])
        print('Total data DDr:', total_data)
        print("")


if __name__ == '__main__':
    executeFL()