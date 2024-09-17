from unzip_file import *;
from data_loading import *;
from avg_age import *;
from top_20_movies import *;
from top_rated_movie import *;
from get_top_10_similar_movies import *;
import json
import pandas as pd
from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
df_user,u_data,u_item,u_genere=data_loading();
def movie_analysis():
    try:
        data = avg_age(df_user);
        logger.info('Average Age Calculation Done');
        print(data);
        print("Avg Age Calculation Done");
        top_20=top_20_movies(u_data,u_item);
        logger.info('Idetified the Top20 Movies');
        print(top_20);
        print("Idetified the Top20 Movies");
    
        top_rated_movies=top_rated_movie(df_user,u_item);
        logger.info('Idetified the Top Rated Movies');
        print(top_rated_movies);
        print("Idetified the Top Rated Movies");
    
        similar_movi=similar_movie();
        logger.info('Top-10 Similar Movies');
        print(similar_movi);
        print("Top-10 Similar Movies");



    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')

movie_analysis()



