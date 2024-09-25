from parameters import Parameters as params
import random

def primary_selected_clients(old_selected_clients, all_clients, round):

    if (len(old_selected_clients) == 0):
        return random.sample(all_clients, int(params.C * params.K))
    
    else:
        sorted_old_clients = sorted(old_selected_clients, key=lambda client: client.goodness, reverse=True)

        
