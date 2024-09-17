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
def sentiment_analysis(text):
    blob = TextBlob(text);
    sentiment = blob.sentiment;
    sentiment_score = sentiment.polarity
    return(sentiment_score)