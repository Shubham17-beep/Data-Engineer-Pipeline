import zipfile
import os
import pandas as pd;
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def unzip_file():
    zip_file_path = 'C://Users//SHUBHAM MADHESIYA//Desktop//premji_invest//TASK2//ml-100k.zip'
    extract_to_folder='C://Users//SHUBHAM MADHESIYA//Desktop//premji_invest//Data_Engineer//dags//scripts'
    # Ensure the extraction folder exists
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)
    
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all contents into the specified folder
        zip_ref.extractall(extract_to_folder)
        print(f'Files extracted to {extract_to_folder}')

unzip_file()