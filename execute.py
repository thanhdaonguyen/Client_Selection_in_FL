
from parameters import Parameters as params
from Initializer import Initializer
from primary_client_selection_methods import primary_selected_clients
from secondary_client_selection_methods import secondary_selected_clients
import random


initializer = Initializer()

# STEP 1: Initialization
all_clients = initializer.initialize_Clients()
server = initializer.initialize_Server()
selected_clients = []

# STEP 2: Enter the training loop
for round in range(params.num_rounds):

    # STEP 3: Resource request

    # STEP 4: Client selection
    pri_clients = primary_selected_clients(selected_clients, all_clients)

    selected_clients = secondary_selected_clients(pri_clients)

    # STEP 5: Model distribution

    # STEP 6: Sccheduled update and upload
    