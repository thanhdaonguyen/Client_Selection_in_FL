


import pandas as pd
import matplotlib.pyplot as plt

data_file_path = [
    "/result_DDr.txt",
    "/result_FedCS.txt"
    "/result_RandCS.txt",
]

y_label = [
    "Number of Clients",
    "Total Training Data",
    "Loss",
    "Acurracy"
]

y_limit = [
    200, 
    10000,
    2,
    1
]

examined_factor = [
    "client_num",
    "data_used",
    "loss",
    "accuracy"
]

data_folder_path = '/Users/thanhdaonguyen/Documents/Thành Đạo/11. Cloud Computing/5. projects/Dao+Thien_PTIT project/Client_Selection_in_FL/results'

def visualizeAllData():

    # Plotting the data
    plt.figure(figsize=(16, 8.1))
    for i in range(4):

        # Read data from the TSV file

        dataDDrCS = pd.read_csv(data_folder_path + '/result_DDrCS.txt', delim_whitespace=True)
        dataFedCS = pd.read_csv(data_folder_path + '/result_FedCS.txt', delim_whitespace=True)
        # dataRandCS = pd.read_csv(data_folder_path + '/result_RandCS.txt', delim_whitespace=True)

        # Plot queueing times
        plt.subplot(2, 2, i + 1)
        plt.plot(dataDDrCS['round'], dataDDrCS[examined_factor[i]], label='DDrCS', color='red', linewidth=1.5)
        plt.plot(dataFedCS['round'], dataFedCS[examined_factor[i]], label='FedCS', color='blue', linewidth=1.5)
        # plt.plot(dataGBO['changing_factor'], dataGBO['efficiency'], label='New Method', linewidth=1.5)
        plt.ylim(0,y_limit[i])
        plt.xlabel("Round", fontsize=8)
        plt.ylabel(y_label[i], fontsize=8)
        title = 'Examining Efficiency in ' + y_label[i]
        plt.title(title, fontsize=8)
        plt.legend(prop={'size': 6})

    # Show the plots
    plt.tight_layout()
    plt.show()
