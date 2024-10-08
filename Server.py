from parameters import *
from model_train import *

def train_on_client(model, client_data, epochs=1):
    model.fit(client_data, epochs=epochs, verbose=0)  #train
    return model.get_weights()  # weight of model

def average_weights(global_weights, client_weights):
    new_weights = []
    for weight in zip(*client_weights):
        new_weights.append(np.mean(np.array(weight), axis=0))  # compute mean of weights
    return new_weights