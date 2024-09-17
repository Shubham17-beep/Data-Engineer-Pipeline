import json
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import warnings
from textblob import TextBlob
# Ignore all warnings
warnings.filterwarnings("ignore")
import sqlite3
import random

def article_scraping(link):
    # Web Scrapping endpoint
    # Send GET request
    links_response = requests.get(link)
    soup = BeautifulSoup(links_response.content, 'html.parser')
    formatted_html = soup.prettify()
    p_tag=soup.find_all('p')
    arcticles=[i.get_text() for i in p_tag]
    complete_article=' '.join(arcticles)
    return complete_article