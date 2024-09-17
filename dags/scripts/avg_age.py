import zipfile
import os
import pandas as pd;
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from data_loading import *;

df_user,u_data,u_item,u_genere=data_loading();

def avg_age(data):
    grouped_df=df_user.groupby('occupation').agg({'age': 'mean'});
    grouped_df.to_csv("Average_age.csv",index=True)
    return(grouped_df)