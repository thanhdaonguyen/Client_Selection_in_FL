from parameters import Parameters as params

class Client:

    def __init__(self):

        self.id = None                         # client id
        self.throughput = []                   # list stores throughput of client in each round (bits/sec)  
        self.data = []                         # list stores number of data samples the client have in each round
        self.computing_speed = []              # list stores the computing speed of clients each round (data samples/sec)
        self.pos_X = 0                         # x coordinate of the client
        self.pos_Y = 0                         # y coordinate of the client

    def get_goodness(self, round):
        return self.get_update_time(round) + self.get_upload_time(round)
    
    def get_update_time(self, round):
        return self.data[round]/self.computing_speed[round]
    
    def get_upload_time(self, round):
        return params.model_size/self.throughput[round]

    def update(self):
        pass 
    


    