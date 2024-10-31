import parameters as pr
import load_data as ld
from model_train import create_keras_model
from tqdm import trange
from Initializer import Initializer
from clients_selection_methods import FedCS_client_selection, DDrCS_client_selection
from federated_learning_operator import examine_data_trained, executeFL
import random
from Utils.visulaizer import visualizeAllData

initializer = Initializer()
# STEP 1: Initialization

def main():
    # Load data

    X_train, X_test, y_train, y_test = ld.get_data()
    all_clients = initializer.initialize_Clients(X_train, y_train)
    old_DDrCS_selected_clients = []

    # STEP 2: Enter the training loop
    print("--------------------Start training -------------------------")
    results_FedCS = {}
    results_DDrCS = {}
    results_RandCS = {}
    global_model_FedCS = create_keras_model()
    global_model_DDrCS = create_keras_model()
    global_model_RandCS = create_keras_model()
    for round in range(pr.num_rounds):

        # STEP 3: Resource request

        # STEP 4: Client selection
        FedCS_selected_clients = FedCS_client_selection(all_clients, round)
        DDrCS_selected_clients = DDrCS_client_selection(old_DDrCS_selected_clients, all_clients, round)
        RandCS_selected_clients = random.sample(all_clients, pr.K)
        old_DDrCS_selected_clients = DDrCS_selected_clients

        # STEP 5: Measure data amount being trained
        data_num_FedCS = examine_data_trained(FedCS_selected_clients, "FedCS")
        data_num_DDrCS = examine_data_trained(DDrCS_selected_clients, "DDr")
        

        # STEP 6: Model training
        loss_FedCS, accuracy_FedCS, global_model_FedCS = executeFL(FedCS_selected_clients, global_model_FedCS, X_test, y_test, round)
        loss_DDrCS, accuracy_DDrCS, global_model_DDrCS = executeFL(DDrCS_selected_clients, global_model_DDrCS, X_test, y_test, round)

        # STEP 7: Save results
        results_FedCS[round] = (len(FedCS_selected_clients), data_num_FedCS, loss_FedCS, accuracy_FedCS)
        results_DDrCS[round] = (len(DDrCS_selected_clients), data_num_DDrCS, loss_DDrCS, accuracy_DDrCS)

        # STEP 8: Logging to terminal
        print("FedCS round", round + 1, ":", results_FedCS[round])
        print("DDrCS round", round + 1, ":", results_DDrCS[round])

        # STEP 9: Save logs
        ld.saveClientsLog(FedCS_selected_clients, round, "FedCS")
        ld.saveClientsLog(DDrCS_selected_clients, round, "DDrCS")
        

    # save data
    ld.saveResultsToFile(results_FedCS, pr.results_file_path + '/result_FedCS.txt')
    ld.saveResultsToFile(results_DDrCS, pr.results_file_path + '/result_DDrCS.txt')


if __name__ == '__main__':
    main()
    visualizeAllData()