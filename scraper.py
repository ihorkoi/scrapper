from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


def get_unian_news_list(url: str):
    req = requests.get(
        url, headers=headers)
    if req.status_code != 200:
        return "Status not 200"
    page = BeautifulSoup(req.text, 'html.parser')
    all_news = page.find_all('div', class_='list-thumbs__item')
    return all_news
