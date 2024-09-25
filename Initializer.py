
from parameters import Parameters as params
from Client import Client
import random


class Initializer:

    def initialize_Clients(self):
        
        clients = []
        for i in range(params.K):
            client = Client()
            client.id = i
            client.pos_X = random.uniform(0, 1)
            client.pos_Y = random.uniform(0, 1)
            client.data_size = random.randint(1, 100)
            client.computing_speed = random.randint(1, 100)
            clients.append(client)

    def initialize_Server(self):
        pass

