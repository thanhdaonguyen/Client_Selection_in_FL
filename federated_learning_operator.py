
def run_learning_process(clients, round, mode):
    if mode == 'FedCS':
        client_ids = [client.id for client in clients]
        print('Running FedCS with clients:', len(client_ids))
        # client_UD_time = [client.get_update_time(round) for client in clients]
        # print('Client update time:', client_UD_time)
        # client_UL_time = [client.get_upload_time(round) for client in clients]
        # print('Client upload time:', client_UL_time)
        total_data = sum([client.data[round] for client in clients])
        print('Total data FedCS:', total_data)

    elif mode == 'DDr':
        client_ids = [client.id for client in clients]
        print('Running DDr with clients:', len(client_ids))
        # client_UD_time = [client.get_update_time(round) for client in clients]
        # print('Client update time:', client_UD_time)
        # client_UL_time = [client.get_upload_time(round) for client in clients]
        # print('Client upload time:', client_UL_time)
        total_data = sum([client.data[round] for client in clients])
        print('Total data DDr:', total_data)
        print("")
