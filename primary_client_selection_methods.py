from parameters import Parameters as params
import random

def primary_client_selection(clients):
    return random.sample(clients, int(params.C * params.K))