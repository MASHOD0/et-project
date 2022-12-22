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