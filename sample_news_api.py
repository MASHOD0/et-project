import requests
import json
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2022-12-20&'
       'sortBy=popularity&'
       'apiKey=431fd6ac7c624e3fbe99eb02a13fb35f')

response = requests.get(url)

print(json.dumps(response.json(), indent=4, sort_keys=True))