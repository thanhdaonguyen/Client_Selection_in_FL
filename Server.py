from parameter import *
class Server:
    def __init__(self):
        self.computing_resource = 0
        self.network_bandwidth = 0
        
    def weight_scalling_factor(clients_trn_data, client_id):
        client_ids = list(clients_trn_data.keys())
    
        # Get the total number of samples across all clients
        global_count = 0
        for client in client_ids:
            client_data = clients_trn_data[client]
            count = 0
            for batch in client_data:
                features, _ = batch  # Unpack features and labels from the tuple
                count += features.shape[0]  # Sum the number of samples in each batch
            global_count += count
        
        # Get the total number of samples for the specific client
        local_count = 0
        for batch in clients_trn_data[client_id]:
            features, _ = batch  # Unpack features and labels from the tuple
            local_count += features.shape[0]  # Sum the number of samples in each batch
        
        # Return the scaling factor (local / global)
        return local_count / global_count


    def scale_model_weights(weight, scalar):
        '''function for scaling a models weights'''
        weight_final = []
        steps = len(weight)
        for i in range(steps):
            weight_final.append(scalar * weight[i])
        return weight_final


    def sum_scaled_weights(scaled_weight_list):
        '''Return the sum of the listed scaled weights. The is equivalent to scaled avg of the weights'''
        avg_grad = list()
        #get the average grad accross all client gradients
        for grad_list_tuple in zip(*scaled_weight_list):
            layer_mean = tf.math.reduce_sum(grad_list_tuple, axis=0)
            avg_grad.append(layer_mean)
            
        return avg_grad


    def test_model(X_test, Y_test,  model, comm_round):
        cce = pr.tf.keras.losses.CategoricalCrossentropy(from_logits=True)
        #logits = model.predict(X_test, batch_size=100)
        logits = model.predict(X_test)
        loss = cce(Y_test, logits)
        acc = accuracy_score(tf.argmax(logits, axis=1), tf.argmax(Y_test, axis=1))
        print('comm_round: {} | global_acc: {:.3%} | global_loss: {}'.format(comm_round, acc, loss))
        return acc, loss