import zipfile
import os
import pandas as pd;
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from data_loading import *;

df_user,u_data,u_item,u_genere=data_loading();
def age_group(age):
    if(age>=0 and age<20):
        age_group='0 to 19';
    elif(age>=20 and age<=25):
        age_group='20 to 25';
    elif(age>=26 and age<=35):
        age_group='26 to 35';
    elif(age>=36 and age<=45):
        age_group='36 to 45';
    elif(age>45):
        age_group='45 and older';
    return(age_group)

def top_rated_movie(df_user,u_item):
    df_user['age_group']=df_user['age'].apply(lambda x : age_group(x));
    u_item_unpivot=u_item.melt(id_vars=['movie id', 'movie title', 'release date','video release date','IMDb URL'],
                      value_vars=u_item.columns[5:],
                          var_name='genre',
                          value_name='genre_flag');
    movie_with_genre=u_item_unpivot[u_item_unpivot['genre_flag']==1].reset_index(drop=True);
    merge_u_data_and_u_user=u_data.merge(df_user,left_on='user id',right_on='user id',how='inner');
    merge_u_data_and_u_user=merge_u_data_and_u_user[['user id','item id','rating','occupation','age_group']];
    merge_u_data_and_u_user_movie=merge_u_data_and_u_user.merge(movie_with_genre,left_on='item id',right_on='movie id',how='inner');
    merge_u_data_and_u_user_movie=merge_u_data_and_u_user_movie[['user id','item id','rating','occupation','age_group','movie title','genre']];
    genre_age_occupation = merge_u_data_and_u_user_movie.groupby(['occupation','genre', 'age_group'])['rating'].mean().reset_index();
    genre_age_occupation.rename(columns={'rating': 'mean_rating'}, inplace=True);
    highest_mean_df = genre_age_occupation.loc[genre_age_occupation.groupby(['occupation','age_group'])['mean_rating'].idxmax()].reset_index(drop=True);
    return(highest_mean_df);