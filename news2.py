import os
import news1
import newsgui
st="top"
genre = {'cricket': "espn-cric-info",
'football': "football-italia",
'science': "national-geographic",
'entertainment': "entertainment-weekly",
'sports': "espn",
'business': "cnbc",
'tech': "engadget",
'gaming': "ign",
'general': "the-times-of-india",
'aus': "abc-news-au",
'uk': "bbc-news",
'us': "the-new-york-times"}
def genre_decode(np):
    return genre[np]
#print news
def printer(dict):
    print dict['title']
    print dict['description']
    print("by -" + str(dict['author']))
def main(a):
    news=news1.caller(genre_decode(a),st)
    return newsgui.news_print(news)
