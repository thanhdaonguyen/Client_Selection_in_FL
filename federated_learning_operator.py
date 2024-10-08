from Client import *
import parameters as pr
from model_train import *
from Server import *
import load_data as ld
import model_train as mt
from tensorflow.keras import backend as K

def executeFL():
    X_train,X_test,y_train,y_test = ld.get_data()
    client_lists = Client.create_clients(X_train,y_train, pr.num_clients, 'clients')  # create clients with random data
    testBatched, clients_batched = ld.batched(X_test,y_test,client_lists)
    global_model = create_keras_model()
    for round_num in range(pr.num_rounds):
        print(f'Round {round_num + 1}/{pr.num_rounds}')
        client_weights = []
        
        # Train model with each client
        for client in range(pr.num_clients):
            print(f'  Training on client {client + 1}/{pr.num_clients}')
            client_model = create_keras_model()  # create model for client
            client_model.set_weights(global_model.get_weights())  # update weights
            weights = train_on_client(client_model, clients_batched[client])  # Training
            client_weights.append(weights)  # Store weight

        # Global weights
        global_weights = average_weights(global_model.get_weights(), client_weights)
        global_model.set_weights(global_weights)  # update global

        for client_id, dataset in testBatched.items():
            print(f'Evaluating global model on Client {client_id} test data:')
            total_loss = 0
            total_accuracy = 0
            num_batches = 0

            for x_batch, y_batch in dataset:
                loss, accuracy = global_model.evaluate(x_batch, y_batch, verbose=0)
                total_loss += loss
                total_accuracy += accuracy
                num_batches += 1

            # Calculate average loss and accuracy
            avg_loss = total_loss / num_batches if num_batches > 0 else 0
            avg_accuracy = total_accuracy / num_batches if num_batches > 0 else 0

            print(f'  Average Loss: {avg_loss:.4f}, Average Accuracy: {avg_accuracy:.4f}')

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