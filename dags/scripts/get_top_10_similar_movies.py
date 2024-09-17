import zipfile
import os
import pandas as pd;
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from data_loading import *;

df_user,u_data,u_item,u_genere=data_loading();

def merge_u_data_and_item(u_data,u_item):
    merged_u_data_item = u_data.merge(u_item, left_on='item id', right_on='movie id', how='inner');
    result_df = merged_u_data_item[['user id', 'movie title', 'rating']].reset_index(drop=True);
    return(result_df)

movies=merge_u_data_and_item(u_data,u_item);

def get_top_10_similar_movies(movie_name, similarity_matrix, threshold=0.95):
    # Get the similarity series for the given movie
    movie_similarity = similarity_matrix[movie_name]
    
    # Remove the movie itself
    movie_similarity = movie_similarity.drop(movie_name)
    
    # Apply the similarity threshold
    similar_movies = movie_similarity[movie_similarity >= threshold]
    
    # Sort by similarity score
    similar_movies = similar_movies.sort_values(ascending=False)
    
    # Select top 10 movies
    return similar_movies.head(10)



def similar_movies(movies):
    user_movie_matrix = movies.pivot_table(index='user id', columns='movie title', values='rating')

# Fill NaN values with 0
    user_movie_matrix = user_movie_matrix.fillna(0)

# Calculate cosine similarity between movies
    similarity_matrix = pd.DataFrame(cosine_similarity(user_movie_matrix.T), 
                                 index=user_movie_matrix.columns, 
                                 columns=user_movie_matrix.columns)

    return(similarity_matrix)

similarity_matrix=similar_movies(movies);


def similar_movie():
    try:
        top_10_similar_movies = get_top_10_similar_movies('Dadetown (1995)', similarity_matrix)
        #print(top_10_similar_movies)
    except Exception as e:
        print("No Such Movie Exist")
    return(top_10_similar_movies)