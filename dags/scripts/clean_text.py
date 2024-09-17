# Function to clean text
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
def clean_text(text):
    # Remove \n, \xa0 and other unwanted characters
    text = re.sub(r'[\n\xa0]', ' ', text)
    
    # Remove emojis (using a Unicode range)
    emoji_pattern = re.compile(
        "[" 
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F700-\U0001F77F"  # alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251" 
        "]+", flags=re.UNICODE)
    
    text = emoji_pattern.sub(r'', text)
    
    # Strip leading/trailing spaces and reduce multiple spaces to a single space
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text