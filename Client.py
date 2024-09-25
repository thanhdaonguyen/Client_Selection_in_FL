class Client:

    def __init__(self):

        self.throughput = 0                    # bits/sec  
        self.data = []                         # list store number of data samples the client have in each round
        self.computing_speed = 0               # data samples/sec
        self.pos_X = 0                         # x coordinate of the client
        self.pos_Y = 0                         # y coordinate of the client

    def get_goodness(self):
        return self.throughput/self.computing_speed

    def update(self):
        pass
    


    