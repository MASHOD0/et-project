from newspaper import Article


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
        