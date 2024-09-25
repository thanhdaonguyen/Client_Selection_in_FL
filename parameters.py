

class Parameters:

    K = 30                              # Number of clients in the system
    C = 0.2                             # Fraction of clients that are selected to participate in each round
    
    num_epochs = 20         
    num_rounds = 5
    T_round = 10

    model_size = 100000000              # Size of the model in bits

    inherited_clients_rate = 0.5
    random_clients_rate = 0.5
