import random
from parameters import Parameters as params


def random_primary_client_selection(all_clients, round):
    #performing the client selection
    return random.sample(all_clients, int(params.C * params.K))

def tactical_primary_client_selection(old_selected_clients, all_clients, round):

    #if it is the first round, select randomly
    if round == 0:
        return random.sample(all_clients, int(params.C * params.K))

    #get the best clients from the previous round
    sorted_old_clients = sorted(old_selected_clients, key=lambda client: client.get_goodness(round - 1), reverse=True)

    best_old_clients = sorted_old_clients[:int(params.inherited_clients_rate * params.C * params.K)]


    #get the rest randomly from the remaining clients
    remaining_clients = []
    for client in all_clients:
        if client not in best_old_clients:
            remaining_clients.append(client)
    new_random_clients = random.sample(remaining_clients, int(params.random_clients_rate * params.C * params.K))

    #return the set K'
    primary_selected_clients = best_old_clients + new_random_clients
    return primary_selected_clients

def get_total_upload_and_update_time(selected_clients, round):

    total_time = 0

    for client in selected_clients:
        client_update_time = client.get_update_time(round)
        client_upload_time = client.get_upload_time(round)

        total_time += max(0, client_update_time - total_time)
        total_time += client_upload_time

    return total_time



def FedCS_client_selection(all_clients, round):
    #select the set K'

    pri_clients = random_primary_client_selection(all_clients, round)

    #select the set S
    select_clients = []

    while (len(pri_clients) > 0):

        best_client = pri_clients[0]
        
        for client in pri_clients:
            time_with_current_client = get_total_upload_and_update_time(select_clients + [client], round)
            time_with_best_client = get_total_upload_and_update_time(select_clients + [best_client], round)

            if time_with_current_client < time_with_best_client:
                best_client = client

        select_clients.append(best_client)
        pri_clients.remove(best_client)

    return select_clients

def DDr_client_selection(old_selected_clients, all_clients, round):
    #select the set K'

    pri_clients = tactical_primary_client_selection(old_selected_clients, all_clients, round)

    #select the set S
    select_clients = []

    while (len(pri_clients) > 0):

        best_client = pri_clients[0]
        
        for client in pri_clients:
            if client.get_goodness(round) > best_client.get_goodness(round):
                best_client = client

        select_clients.append(best_client)
        select_clients = sorted(select_clients, key=lambda client: client.get_update_time(round), reverse=False)
        
        pri_clients.remove(best_client)

    return select_clients
