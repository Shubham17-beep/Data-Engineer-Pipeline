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
from clean_text import *;
from article_scraping import *;
from sentiment_analysis import *;
from get_web_scraping_links import *;

def final():
    ticker=["HDFC","Tata Motors"];
    column=['post_url','cover_image','title','excerpt','published_date','query']
    complete_data=pd.DataFrame(columns=column)
    for tick in ticker:
        data=get_web_scraping_links(tick);
        data_json=data.json;
        entry=[];
        for i in data_json()['matches']:
            frame=[i["post_url"],i["cover_image"],i["title"],i["excerpt"],i["published_date"],tick];
            entry.append(frame)
        df=pd.DataFrame(entry,columns=column)
        df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        df['published_date']=df['published_date'].apply(lambda x : x[:10])
        df_sorted=df.sort_values(by='published_date', ascending=False)
        df_sorted_5=df_sorted.head(5)
        complete_data = pd.concat([complete_data,df_sorted_5], ignore_index=True)
    complete_data['Complete_Article']=complete_data['post_url'].apply(lambda x : article_scraping(x));
    complete_data['Complete_Article']=complete_data['Complete_Article'].apply(lambda x : clean_text(x));
    complete_data['Sentiment']=complete_data['Complete_Article'].apply(lambda x : sentiment_analysis(x));
    print("I am here")
    return(complete_data)

final()