import numpy as np
import random
import cv2
import os
from imutils import paths
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score

import tensorflow as tf
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten

dataset_file_path = os.path.join(os.path.dirname(__file__),'datasets\mnist')
results_file_path = os.path.join(os.path.dirname(__file__),'results')

lr = 0.01 
loss='categorical_crossentropy'
metrics = ['accuracy']
optimizer = SGD(learning_rate=lr, 
                decay=lr / num_rounds, 
                momentum=0.9
               )          

K = 1000                              # Number of clients in the system
C = 0.3                           # Fraction of clients that are selected to participate in each round

num_epochs = 20    
num_rounds = 10
T_round = 360

model_size = 5000000000              # Size of the model in bits

inherited_clients_rate = 0.5
random_clients_rate = 0.5


