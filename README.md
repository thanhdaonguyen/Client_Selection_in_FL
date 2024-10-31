# Client_Selection_in_FL
This is implementation for paper DOI: 10.1109/ICC.2019.8761315

## Code base structure


- `execute.py`: The file operating the whole process
- `parameter.py`: The file containing all the parameters of the system
- `dataset/`: This is the folder containing the data used for training. Data must be accessed easily as a list.
- `results/`: This is the folder containing all testing results
    - `accuracy/`: Show accuracy of protocols as number of rounds increases
    - `number_of_clients/`: Show number of clients in protocols each round
    - `data_trained/`: Show number of data sample protocols utilized each round
    - Each result folder includes these files: 
        - `Naive_protocol.txt`: Result of naive protocol
        - `FedCS_protocol.txt`: Result of FedCS protocol
        - `New_prototol.txt`: Result of New protocol
- `Client.py`: The class used for representing clients
- `Server.py`: The class used for representing server
- `client_selection_methods.py`: The file implementing all client selection methods
- `Utils/`: Folder containing useful tools for simulation of the paper.
    - `fluctuated_data_generator.py`: The file containing a function to randomly create data at clients for each round. 

## Workflow

To operate, run the file `execute.py`. The workflow in the file follows following steps:

1. **Initialization**: 
    - The code starts by initializing: clients (set $K$), server, selected client list (set $\mathbb{S}$) --> `execute.py` 
    - Detail steps for performing the initialization --> `Initializer.py`
  
2. **Enter the training loop**:
    - The process enter a loop of Resource Request, Client selection, Distribution, Scheduled Update & Upload, and Aggregation (just like the described protocol in the according paper). Details are described in the following steps

3. **Resource Request** 
    - <mark>Right now, just assume that the server knows in advance all information of clients. Therefore this step is ignored</mark>


4. **Client selection**
    - This step will apply the two method FedCS and DDr to select clients. The selected sets of two methods will be used for simulation in following steps
    - First, the primary-selected clients (set $K'$) is chosen from the intialized clients (set $K$) --> `clients_selection_methods.py`.
    - Then, the secondary-selected clients (set $\mathbb{S}$) is chosen form primary-selected clients (set $K'$) --> `clients_selection_methods.py`.

5. **Distribution**
    - This step only accounts for the calculattion of the time used for global model distribution --> `execute.py`

6. **Scheduled Update & Upload** 
    - From the secondary-selected clients (set $\mathbb{S}$) got from step 4, we know perform the training process at each selected client.
    - Update (<mark>The details will be determined in the future. But the idea is:</mark>)
        - The data size in each selected cliented is examined and that client will be allocated the exact amount of data from the dataset (Note that each data sample can only be allocated once in the whole process)
        - We then run the learning process in each clients to output their models in a list
        - The results of this learning (accuracy) is then stored
    - Upload (<mark>This step is ignore as we are just simulating in a sole machine. Therefore doesn't need to "upload" to anywhere else</mark>)

7. **Aggregation**
    - This step calculate the global model attained after aggregating models from all clients.
    - The accuracy result is stored.


