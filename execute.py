from Client import *
import parameter as pr
from model_train import *
from Server import *
import load_data as ld
import model_train as mt
from tensorflow.keras import backend as K

def executeFL():
    X_train,X_test,y_train,y_test = ld.get_data()
    client_lists = Client.create_clients(X_train,y_train, 12, 'clients')  # create clients with random data
    testBatched, clients_batched = ld.test_batched(X_test,y_test,client_lists)
    smlp_global = mt.SimpleMLP()
    global_model = smlp_global.build(784, 10)
    for comm_round in range(pr.comms_round):
            
        # get the global model's weights - will serve as the initial weights for all local models
        global_weights = global_model.get_weights()
        #initial list to collect local model weights after scalling
        scaled_local_weight_list = list()
        
        #loop through each client and create new local model
        for client_id in client_lists:
            smlp_local = mt.SimpleMLP()
            local_model = smlp_local.build(784, 10)
            local_optimizer = pr.optimizer.__class__(**pr.optimizer.get_config())
            local_model.compile(loss=pr.loss, 
                        optimizer=local_optimizer, 
                        metrics=pr.metrics)
            
            #set local model weight to the weight of the global model
            local_model.set_weights(global_weights)
            
            #fit local model with client's data
            local_model.fit(clients_batched[client_id], epochs=1, verbose=0)
            
            #scale the model weights and add to list
            scaling_factor = Server.weight_scalling_factor(clients_batched, client_id)
            scaled_weights = Server.scale_model_weights(local_model.get_weights(), scaling_factor)
            scaled_local_weight_list.append(scaled_weights)
            
            #clear session to free memory after each communication round
            K.clear_session()
            
        #to get the average over all the local model, we simply take the sum of the scaled weights
    average_weights = Server.sum_scaled_weights(scaled_local_weight_list)
    
    #update global model 
    global_model.set_weights(average_weights)

    #test global model and print out metrics after each communications round
    for(X_test, Y_test) in testBatched:
        global_acc, global_loss = Server.test_model(X_test, Y_test, global_model, comm_round)
        
from parameters import Parameters as params
from Initializer import Initializer
from clients_selection_methods import FedCS_client_selection, DDr_client_selection
from federated_learning_operator import run_learning_process
import random

initializer = Initializer()

# STEP 1: Initialization
all_clients = initializer.initialize_Clients()
server = initializer.initialize_Server()
old_DDr_selected_clients = []

# STEP 2: Enter the training loop
for round in range(params.num_rounds):

    # STEP 3: Resource request

    # STEP 4: Client selection
    FedCS_selected_clients = FedCS_client_selection(all_clients, round)
    DDr_selected_clients = DDr_client_selection(old_DDr_selected_clients, all_clients, round)
    old_DDr_selected_clients = DDr_selected_clients

    # STEP 5: Model distribution
    
    # STEP 6: Sccheduled update and upload

    run_learning_process(FedCS_selected_clients, round, 'FedCS')
    run_learning_process(DDr_selected_clients, round, 'DDr')
