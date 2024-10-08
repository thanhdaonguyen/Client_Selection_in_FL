
import parameters as pr
from Client import Client
from Server import Server
from Utils.fluctuated_data_generator import flucPointGenerator
import random


class Initializer:

    def initialize_Clients(self):
        
        clients = []
        for i in range(pr.K):
            client = Client()
            client.id = i
            client.pos_X = random.uniform(0, 1)
            client.pos_Y = random.uniform(0, 1)
            client.data = flucPointGenerator(100,1000,pr.num_rounds)
            client.computing_speed = flucPointGenerator(10,100,pr.num_rounds)
            client.throughput = flucPointGenerator(50000000,1000000000,pr.num_rounds)
            clients.append(client)

        return clients

    def initialize_Server(self):
        
        server = Server()
        server.id = 0
        server.pos_X = random.uniform(0, 1)
        server.pos_Y = random.uniform(0, 1)
        return server

