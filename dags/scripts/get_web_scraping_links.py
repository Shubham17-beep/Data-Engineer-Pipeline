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
def get_web_scraping_links(ticker):
    # Web Scrapping endpoint
    web_url = f"https://backend.finshots.in/backend/search/?q={ticker}"
    # Send GET request
    links_response = requests.get(web_url)
    return links_response