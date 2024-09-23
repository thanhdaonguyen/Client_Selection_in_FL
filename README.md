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