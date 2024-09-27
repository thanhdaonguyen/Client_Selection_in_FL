import parameter as pr
class Client:
    def __init__(self,id,computing_resource,network_bandwidth):
        self.id = id
        self.computing_resource = computing_resource
        self.network_bandwidth = network_bandwidth
        self.data = None
    
    def create_clients(image_list, label_list, num_clients, initial='clients'):
        client_list ={} 
        for i in range(num_clients):
            id = i
            computing_resource = pr.random.randint(1,100)
            network_bandwidth = pr.random.randint(1,100)
            new_client = Client(id, computing_resource, network_bandwidth)
            client_list[new_client.id]=new_client

        #randomize the data
        data = list(zip(image_list, label_list))
        pr.random.shuffle(data)
        
        #shard data and place at each client
        size = len(data)//num_clients
        shards = [data[i:i + size] for i in range(0, size*num_clients, size)]
        
        #number of clients must equal number of shards
        assert(len(shards) == len(client_list))
        for i in range(len(client_list)):
            client_list[i].data = shards[i] 
        print("-----------------Done create clients with it own data-----------------")
        return client_list

    