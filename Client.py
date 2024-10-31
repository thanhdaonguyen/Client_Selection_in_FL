import parameters as pr
class Client:
    def __init__(self):
        self.id = id                             # client id
        self.computing_resource = 0           # list stores the computing speed of clients each round (data samples/sec)
        self.through_put = 0 # list stores throughput of client in each round (bits/sec)               
        self.data = None  # list data samples the client have 
        self.model = None  # model of client
            
                                              

    def get_goodness(self, round):
        return len(self.data) / (self.get_update_time(round) + self.get_upload_time(round))
    
    def get_update_time(self, round):
        return len(self.data) / self.computing_speed[round]
    
    def get_upload_time(self, round):
        return pr.model_size / self.throughput[round]

    def update(self):
        pass 

    def create_clients(image_list, label_list, num_clients, initial='clients'):
        client_list ={} 
        for i in range(num_clients):
            id = i
            computing_resource = pr.random.randint(1,100)
            throughput = pr.random.randint(1,100)
            new_client = Client(id, computing_resource, throughput)
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
