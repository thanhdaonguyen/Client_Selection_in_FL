
from parameters import Parameters as params
from Client import Client
from Server import Server
from Utils.fluctuated_data_generator import flucPointGenerator
import random


class Initializer:

    def initialize_Clients(self):
        
        clients = []
        for i in range(params.K):
            client = Client()
            client.id = i
            client.pos_X = random.uniform(0, 1)
            client.pos_Y = random.uniform(0, 1)
            client.data = flucPointGenerator(10,100,100)
            client.computing_speed = flucPointGenerator(10,100,100)
            client.throughput = flucPointGenerator(10,100,100)
            clients.append(client)

        return clients

    def initialize_Server(self):
        
        server = Server()
        server.id = 0
        server.pos_X = random.uniform(0, 1)
        server.pos_Y = random.uniform(0, 1)
        return server

