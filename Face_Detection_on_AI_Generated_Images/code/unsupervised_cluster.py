import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from hdf5storage import loadmat
import os
from PIL import Image

BASE_PATH = '../'
DATA_FILE = 'data/combined_data_normalized.csv'
DATA_FILE_2 = 'data/output/combined_data_mtx.csv'
MAT_FILE = 'data/combined_data_mtx.mat'

if __name__ == '__main__':

    combined_data_mtx = loadmat(BASE_PATH + MAT_FILE)

    # Prepare labels
    # Split the dataset into training and testing sets
    # X = np.array(combined_data_mtx['img_array'].tolist())  # Convert list of arrays to a numpy array
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(combined_data_mtx)

    # print(dict(combined_data_mtx[['bool_label', 'label', 'difficulty', 'img_array', 'img_array2']]))
