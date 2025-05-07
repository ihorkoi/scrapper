import requests
from bs4 import BeautifulSoup
# rewrite


def extract_text_from_news(link):
    req = requests.get(link, headers=headers)
    if req.status_code != 200:
        raise RuntimeError("Status not 200")
    page = BeautifulSoup(req.text, 'html.parser')
    raw_text = page.find('div', class_='article-text')
    try:
        text = '\n'.join([x.getText() for x in raw_text.find_all('p')])
    except:
        raise RuntimeError('Something goes wrong!')
    return text


def prepare_news_object(news_item):
    print(f"Processing: {news_item.a['href']}")
    news = {'title': '', 'text': '', 'creation_time': '', 'reference': ''}

    news["title"] = news_item.find('h3').getText().strip()
    news["text"] = extract_text_from_news(news_item.a['href'])
    news["creation_time"] = news_item.find(
        'div', class_='list-thumbs__time time').getText()
    news['reference'] = news_item.a['href'].strip()

    return news
