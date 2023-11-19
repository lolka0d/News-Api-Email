import requests
import configparser

from send_email import send_email

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['NEWS']['KEY']

topic = "tesla"
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       f"from=2023-10-19&"
       f"sortBy=publishedAt&"
       f"language=en&"
       f"apiKey={api_key}")

req = requests.get(url)
response = req.json()
content = "Subject: Today's News:\n"
for article in response['articles'][:20]:
    if article['description'] is not None:
        content += article['title'] + '\n' \
                   + article['description'] + '\n' + article['url'] + '\n\n'

content = content.encode('utf-8')
print(send_email(content))
