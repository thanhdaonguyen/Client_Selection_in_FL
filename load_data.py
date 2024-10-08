import parameters as pr

def load(imgpath, paths, verbose=-1):
    data = list()
    labels = list()
    # loop over the input images
    for (i, imgpath) in enumerate(paths):
        # load the image and extract the class labels
        im_gray = pr.cv2.imread(imgpath, pr.cv2.IMREAD_GRAYSCALE)
        image = pr.np.array(im_gray).flatten()
        label = imgpath.split(pr.os.path.sep)[-2]
        # scale the image to [0, 1] and add to list
        data.append(image/255)
        labels.append(label)
        # show an update every `verbose` images
        if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
            print("[INFO] processed {}/{}".format(i + 1, len(paths)))
    # return a tuple of the data and labels
    return data, labels

def batch_data(data_shard, bs=32):
    #seperate shard into data and labels lists
    data, label = zip(*data_shard)
    dataset = pr.tf.data.Dataset.from_tensor_slices((list(data), list(label)))
    return dataset.shuffle(len(label)).batch(bs)

def test_batched(X_test,y_test,clients):
    clients_batched = dict()
    for (client_id, client) in clients.items():
        clients_batched[client_id] = batch_data(client.data)
    return pr.tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(len(y_test)),clients_batched

def get_data():
    #declare path to your mnist data folder
    img_path = pr.dataset_file_path + '\\trainingSet'
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