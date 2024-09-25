
from parameters import Parameters as params
from Initializer import Initializer


initializer = Initializer()

# STEP 1: Initialization
clients = initializer.initialize_Clients()
server = initializer.initialize_Server()

# STEP 2: Enter the training loop
for round in range(params.num_rounds):

    # STEP 3: Resource request

    # STEP 4: Client selection

    # STEP 5: Model distribution

    # STEP 6: Sccheduled update and upload
    selected_clients = random.sample(clients, int(params.C * params.K))
    for client in selected_clients:
        client.compute()
        server.aggregate(client)
    server.update()
    for client in clients:
        client.update()
    server.send_model_to_clients(clients)
    print("Round ", round, " done.")