import zipfile
import os
import pandas as pd;
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def data_loading():
    user_col=['user id','age','gender','occupation','zip code'];
    df_user=pd.read_csv('C://Users//SHUBHAM MADHESIYA//Desktop//premji_invest//TASK2//ml-100k//u.user',sep='|',header=None);
    df_user.columns=user_col;
    u_data=pd.read_csv('C://Users//SHUBHAM MADHESIYA//Desktop//premji_invest//TASK2//ml-100k//u.data',sep='\t',header=None)
    u_data_col=['user id','item id','rating','timestamp'];
    u_data.columns=u_data_col;
    u_item=pd.read_csv('C://Users//SHUBHAM MADHESIYA//Desktop//premji_invest//TASK2//ml-100k//u.item',sep='|',encoding='iso-8859-1',header=None);
    item_col=['movie id','movie title','release date','video release date',
              'IMDb URL','unknown','Action','Adventure','Animation',
              'Childrens','Comedy','Crime','Documentary','Drama','Fantasy'
              ,'Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi',
              'Thriller','War','Western'];
    u_item.columns=item_col;
    u_genere=pd.read_csv('C://Users//SHUBHAM MADHESIYA//Desktop//premji_invest//TASK2//ml-100k//u.genre',sep='|',header=None);
    genre_col=['genre','genre_id'];
    u_genere.columns=genre_col;
    return(df_user,u_data,u_item,u_genere)