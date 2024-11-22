import pandas as pd
import numpy as np
import os
from PIL import Image
from scipy.io import savemat
# from hdf5storage import savemat

BASE_PATH = '../'
DATA_FILE = 'data/output/combined_data.csv'


def get_img_array(image_file: str):
    if os.path.exists(BASE_PATH + image_file):
        image_obj = Image.open(BASE_PATH + image_file)
        image_obj = image_obj.convert("L")
        image_obj = (np.round(np.array(image_obj).reshape(-1, 1) / 255, 6)).ravel()
    else:
        image_obj = None

    return image_obj


if __name__ == '__main__':

    df = pd.read_csv(BASE_PATH + DATA_FILE)

    df['img_array'] = df['file_path'].apply(get_img_array)
    df['bool_label'] = df['label'].apply(lambda x: 1 if x == 'real' else 0).values

    reduced_df = dict()
    for col in ['bool_label', 'label', 'difficulty']:
        reduced_df[col] = df[col].values

    reduced_df['img_array'] = np.array(np.vstack(df['img_array'].values), dtype=np.float32)

    # savemat(BASE_PATH + 'data/combined_data_mtx.mat', reduced_df, format=7.3, truncate_existing=True)
    savemat(BASE_PATH + 'data/combined_data_mtx.mat', reduced_df, format='5', do_compression=True)
