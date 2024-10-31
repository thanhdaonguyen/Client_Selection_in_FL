
import parameters as pr
import load_data as ld
from Client import Client
from Utils.fluctuated_data_generator import flucPointGenerator
import random
from Utils.probability_generator import generate_probabilities
from model_train import create_keras_model


class Initializer:

    def initialize_Clients(self, img_list, label_list):

        #randomize the data
        data = list(zip(img_list, label_list))
        pr.random.shuffle(data)

        #shard data and place at each client
        client_data_proportion = generate_probabilities(pr.K)

        # Calculate the size of each shard based on the probabilities
        total_size = len(data)
        shard_sizes = [1] * pr.K  # Initialize each shard size with at least 1
        remaining_size = total_size - pr.K  # Remaining data size after initial allocation

        # Distribute the remaining data proportionally
        proportional_sizes = [int(remaining_size * proportion) for proportion in client_data_proportion]

        # Ensure the sum of proportional sizes equals the remaining size
        proportional_sizes[-1] += remaining_size - sum(proportional_sizes)

        # Add the proportional sizes to the initial shard sizes
        shard_sizes = [initial + proportional for initial, proportional in zip(shard_sizes, proportional_sizes)]


        # Allocate data to shards
        shards = []
        start_index = 0
        for size in shard_sizes:
            end_index = start_index + size
            shards.append(data[start_index:end_index])
            start_index = end_index

        # size = len(data) // pr.K
        # shards = [data[i:i + size] for i in range(0, size * pr.K, size)]
                
        clients = []
        for i in range(pr.K):
            client = Client()
            client.id = i
            client.pos_X = random.uniform(0, 1)
            client.pos_Y = random.uniform(0, 1)
            client.data = shards[i]
            client.computing_speed = flucPointGenerator(pr.computing_speed_range[0],pr.computing_speed_range[1],pr.num_rounds)
            client.throughput = flucPointGenerator(pr.throughput_range[0],pr.throughput_range[1],pr.num_rounds)
            client.model = create_keras_model()
            clients.append(client)

        assert(len(shards) == len(clients))
        print("-----------------Done create clients with it own data-----------------")

        return clients

    

