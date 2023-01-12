import requests
import json
import os
import sys
from newspaper import Article
import smtplib
import re

class Summary_Generator:
    """
    This class generates the summary of the news article
    """
    def __init__(self, url, lang):
        self.url = url
        self.lang = lang
        self.summary = self.generate_summary()

    def generate_summary(self):
        """
        generates summary of the news article
        """
        article = Article(self.url, language=self.lang)
        article.download()
        article.parse()
        article.nlp()
        summary = article.summary
        
        return summary
        

class Data_Fetch:
    """
    This class fetches data from the APIs/RSS feeds/HTML Scrapped from the internet
    """
    def __init__(self, url):
        self.url = url
        self.data_from_api = self.fetch_news_from_api()
        # self.data_from_rss = self.fetch_news_from_rss()
        # self.data_from_html = self.fetch_news_from_html()

    def fetch_news_from_api(self):
        """
        fetches info from news API
        """
        
        response = requests.get(self.url) # getting data from the url
        data_json = json.dumps(response.json(), indent=4) # reciving data in json format
        data = json.loads(data_json) # converting json data to python dictionary
        return data


    def fetch_news_from_rss(self):
        """
        fetches info from RSS feeds
        """
        pass
    def fetch_news_from_html(self):
        """
        fetches info from HTML scrapped
        """
        pass


class Url_Generator:
    """
    This class generates the url for the APIs/RSS feeds/HTML to be Scrapped from the internet
    """
    def __init__(self, key, sort, date, query):
        self.key = key
        self.sort = sort
        self.date = date
        self.query = query
        self.url = self.generate_url()

    def generate_url(self):
        """
        generates url for the APIs/RSS feeds/HTML to be Scrapped from the internet
        """
        api_key = f'apiKey={self.key}'
        sort_by = f'sortBy={self.sort}&'
        from_date = f'from={self.date}&'
        language = 'language=en&'
        api_query = f'q={self.query}&'
        api_url = 'https://newsapi.org/v2/everything?'
        url = api_url+api_query+from_date+language+sort_by+api_key
        return url



if __name__ == "__main__":
    def safe_str(obj):
        try: return str(obj)
        except UnicodeEncodeError:
            return obj.encode('ascii', 'ignore').decode('ascii')
        return ""

    s = smtplib.SMTP('smtp.outlook.com', 587)
    key = '431fd6ac7c624e3fbe99eb02a13fb35f'
    sort = 'popularity'
    date = '2023-1-8'
    query = 'football'



    Url_Generator = Url_Generator(key, sort, date, query)
    url = Url_Generator.generate_url()

    Data_Fetch = Data_Fetch(url)
    data = Data_Fetch.fetch_news_from_api()
    s.starttls()
    s.login("newsrpa@outlook.com", "Rida@123")
    message = "Hello, subscriber"+'\n'
    # print(data)
    article_count = 0
    for d in data['articles']:
        if d['url'] is not None and article_count <= 5:
            # print(d['title'])
            safe_title = safe_str(d['title'])
            message = message + safe_title + '\n'
            # print(d['description'])
            safe_description = safe_str(d['description'])
            message = message + safe_description + '\n'
            # print(d['url'])
            safe_url = safe_str(d['url'])
            message = message + safe_url + '\n'
            # print('---------------------------------summary---------------------------------')
            message = message + '---------------------------------summary---------------------------------'+'\n'+ '\n'
            su = Summary_Generator(d['url'], 'en')
            summary = Summary_Generator.generate_summary(su)
            # print(summary)
            safe_summary = safe_str(summary)
            message = message + safe_summary + '\n'
            # print('--------------------------------------------------------------------------')
            message = message + '--------------------------------------------------------------------------'+ '\n'+ '\n'
            article_count += 1
    # print(message)
    filtered_message = re.sub(r'[^\x00-\x7F]+',' ', message)
    print(filtered_message)
    s.sendmail("newsrpa@outlook.com", 'mashhood2002@gmail.com', filtered_message)
    s.quit()
    # breydwcuzdhefngp