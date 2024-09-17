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
def persist_data(df):
    # Create a connection to the database
    conn = sqlite3.connect('sentiment.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SentimentScores (
        title TEXT,
        sentiment_score REAL,
        query TEXT
            )
        ''')
    # Insert data into the SQL table
    for index, row in df.iterrows():
          cursor.execute('''
            INSERT INTO SentimentScores (title, sentiment_score, query)
            VALUES (?, ?, ?)
            ''', (row['title'], row['Sentiment'], row['query']))  

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()