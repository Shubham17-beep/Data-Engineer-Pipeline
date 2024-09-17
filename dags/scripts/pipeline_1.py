from final import *;
from clean_text import *;
from article_scraping import *;
from sentiment_analysis import *;
from persist_data import *;
from get_web_scraping_links import *;
import json
import pandas as pd
from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def hdfc_tatamotor_sentiment_pipeline():
    try:
        data = final()
        logger.info('Complete and Cleaned DataFrame with Title,Sentiment using textblob and Query');
        #insert the data into table
        persist_data(data)
        logger.info('Data Inserted Successfully.')
        print("Data Inserted Successfully");

    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')

hdfc_tatamotor_sentiment_pipeline()



