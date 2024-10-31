from parameters import *
from model_train import *

def train_on_client(model, client_data, epochs=5):
    model.fit(client_data, epochs=epochs, verbose=0)  #train
    return model.get_weights()  # weight of model

def average_weights(client_weights):
    new_weights = []
    total_data = sum([w[1] for w in client_weights])
    
    for i in range(len(client_weights[0][0])):
        layer_weights = np.array([client_weights[j][0][i] * client_weights[j][1] for j in range(len(client_weights))])
        new_weights.append(np.sum(layer_weights, axis=0) / total_data)
        

    return new_weights