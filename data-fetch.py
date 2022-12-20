import requests
import json
import os
import sys
class Data_Fetch:
    """
    This class fetches data from the APIs/RSS feeds/HTML Scrapped from the internet
    """
    def __init__(self, url):
        self.url = url
        
    def fetch_news_from_api(self):
        """
        fetches info from news API
        """
        
        response = requests.get(self.url) # getting data from the url
        data = json.dumps(response.json(), indent=4) # reciving data in json format
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

