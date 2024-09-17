import zipfile
import os
import pandas as pd;
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from data_loading import *;

df_user,u_data,u_item,u_genere=data_loading();

def top_20_movies(u_data,u_item):
    count_df = u_data.groupby(['item id']).size().reset_index(name='count').sort_values(by='count',ascending=False);
    count_df=count_df[count_df['count']>=35].reset_index(drop=True)
    top_20_item_id=count_df.head(20);
    merged_df = u_item.merge(top_20_item_id, left_on='movie id', right_on='item id', how='inner');
    result_df = merged_df[['movie id', 'movie title', 'count']].sort_values(by='count',ascending=False).reset_index(drop=True);
    top_20_movies=result_df.head(20);
    top_20_movies.to_csv("top_20_movies.csv",index=False)
    return(top_20_movies)