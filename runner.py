from DataFetch import Data_Fetch
from UrlGenerator import Url_Generator
from SummaryGenerator import Summary_Generator
# from pdf-writer import Pdf_Writer
# from email-sender import Email_Sender


if __name__ == "__main__":

    key = '431fd6ac7c624e3fbe99eb02a13fb35f'
    sort = 'popularity'
    date = '2022-12-20'
    query = 'Fifa worldcup'



    Url_Generator = Url_Generator(key, sort, date, query)
    url = Url_Generator.generate_url()

    Data_Fetch = Data_Fetch(url)
    data = Data_Fetch.fetch_news_from_api()
    # print(data)
    for d in data['articles']:
        if d['url'] is not None:
            print(d['title'])
            print(d['description'])
            print(d['url'])
            print('---------------------------------summary---------------------------------')
            su = Summary_Generator(d['url'], 'en')
            summary = Summary_Generator.generate_summary(su)
            print(summary)
            print('--------------------------------------------------------------------------')

    # for d in data:
    #     Summary_Generator = Summary_Generator(d)
    #     summary = Summary_Generator.generate_summary()
    #     Pdf_Writer = Pdf_Writer(summary)

    # Pdf_Writer.write_pdf()
    # Pdf_Writer.save_pdf_to_aws_s3()

    # Email_Sender = Email_Sender()
    # Email_Sender.send_email()