

class Parameters:

    K = 1000                              # Number of clients in the system
    C = 0.3                           # Fraction of clients that are selected to participate in each round
    
    num_epochs = 20    
    num_rounds = 5
    T_round = 360

    model_size = 5000000000              # Size of the model in bits

    inherited_clients_rate = 0.5
    random_clients_rate = 0.5
