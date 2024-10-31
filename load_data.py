import parameters as pr
from tqdm import tqdm
def load(imgpath, paths, verbose=-1):
    data = list()
    labels = list()
    # loop over the input images
    for i, imgpath in tqdm(enumerate(paths), total=len(paths), desc="Loading data:"):
        # load the image and extract the class labels
        im_gray = pr.cv2.imread(imgpath, pr.cv2.IMREAD_GRAYSCALE)
        image = pr.np.array(im_gray).flatten()
        label = imgpath.split(pr.os.path.sep)[-2]
        # scale the image to [0, 1] and add to list
        data.append(image/255)
        labels.append(label)
    # return a tuple of the data and labels
    return data, labels

def batch_data(data_shard, bs=32):
    #seperate shard into data and labels lists
    data, label = zip(*data_shard)
    dataset = pr.tf.data.Dataset.from_tensor_slices((list(data), list(label)))
    return dataset.shuffle(len(label)).batch(bs)

def batched(clients):
    clients_batched = dict()
    for i in range(len(clients)):
        clients_batched[i] = batch_data(clients[i].data)
    return clients_batched


def get_data():
    #declare path to your mnist data folder
    img_path = pr.dataset_file_path + '/trainingSet'

    #get the path list using the path object
    image_paths = list(pr.paths.list_images(img_path))

    #apply our function
    image_list, label_list = load(img_path,image_paths, verbose=10000)
    
    #binarize the labels
    lb = pr.LabelBinarizer()
    label_list = lb.fit_transform(label_list)

    #split data into training and test set
    X_train, X_test, y_train, y_test = pr.train_test_split(image_list, label_list, test_size=0.1, random_state=42)
    return X_train, X_test, y_train, y_test

def saveResultsToFile(results, filename):

    
    # Tạo thư mục nếu nó không tồn tại
    directory = pr.results_file_path
    pr.os.makedirs(directory, exist_ok=True)
    
    # Mở file để ghi
    with open(filename, 'w') as f:
        # Ghi tiêu đề cột
        f.write(f"{'round':<6} {'client_num':<15} {'data_used':<15} {'loss':<15} {'accuracy':<15} \n")
        
        # Ghi dữ liệu
        for round_num, (clients_num, data_used, avg_loss, avg_accuracy) in results.items():
            f.write(f"{round_num + 1:<6} {clients_num:<15.4f} {data_used:<15.4f} {avg_loss:<15.4f} {avg_accuracy:<15.4f} \n")

def saveClientsLog(clients_list, round, mode):

    # Tạo thư mục nếu nó không tồn tại
    directory = pr.results_file_path
    directory = pr.results_file_path
    pr.os.makedirs(directory, exist_ok=True)

    if mode == "FedCS": directory += '/clients_log/FedCS'
    elif mode == "DDrCS": directory += '/clients_log/DDrCS'
    elif mode == "RandCS": directory += '/clients_log/RandCS'
    
    filepath = directory + f'/round_{round+1}.txt'
    # Mở file để ghi
    with open(filepath, 'w') as f:
        # Ghi tiêu đề cột
        f.write(f"{'client':<6} {'data':<15} {'computing_speed':<15} {'throughput':<15} {'update_time':<15} {'upload_time':<15}\n")
        
        # Ghi dữ liệu
        for i, client in enumerate(clients_list):
            f.write(f"{i:<6} {len(client.data):<15.4f} {client.computing_speed[round]:<15.4f} {client.throughput[round]:<15.4f} {client.get_update_time(round):<15.4f} {client.get_upload_time(round):<15.4f}\n")