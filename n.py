import requests
import json
import sys
import os
def printer(dict):
    print dict['title']
    print dict['description']
    print("by -" + str(dict['author']))
def caller(news_source,sortby):
    response = requests.get("https://newsapi.org/v1/articles?source="+ news_source + "&sortBy="+ sortby +"&apiKey=892ee34b561e4c22b22eb017cc6ca3c2")
    news_data = json.loads(response.text)
    news = news_data['articles']
    return news
