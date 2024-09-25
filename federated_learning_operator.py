
def run_learning_process(clients, mode):
    if mode == 'FedCS':
        client_ids = [client.id for client in clients]
        print('Running FedCS with clients:', client_ids)
    elif mode == 'DDr':
        client_ids = [client.id for client in clients]
        print('Running DDr with clients:', client_ids)
