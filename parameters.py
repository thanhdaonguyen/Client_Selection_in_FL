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
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  # Suppress INFO logs
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations
dataset_file_path = os.path.join(os.path.dirname(__file__),'datasets\mnist')
results_file_path = os.path.join(os.path.dirname(__file__),'results')

num_epochs = 20    
num_rounds = 10
T_round = 360
num_clients = 10

model_size = 5000000000              # Size of the model in bits

inherited_clients_rate = 0.5
random_clients_rate = 0.5


K = 1000                             # Number of clients in the system
C = 0.3                              # Fraction of clients that are selected to participate in each round



