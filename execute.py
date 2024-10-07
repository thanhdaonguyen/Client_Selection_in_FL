import parameters as pr pr
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
for round in range(pr.num_rounds):

    # STEP 3: Resource request

    # STEP 4: Client selection
    FedCS_selected_clients = FedCS_client_selection(all_clients, round)
    DDr_selected_clients = DDr_client_selection(old_DDr_selected_clients, all_clients, round)
    old_DDr_selected_clients = DDr_selected_clients
    # STEP 5: Model distribution

    
    # STEP 6: Sccheduled update and upload

    run_learning_process(FedCS_selected_clients, round, 'FedCS')
    run_learning_process(DDr_selected_clients, round, 'DDr')
