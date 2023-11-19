import requests
import os

from send_email import send_email

api_key = os.getenv("API_KEY")
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-19&sortBy=publishedAt&apiKey=" + api_key

req = requests.get(url)
response = req.json()
content = ""
for article in response['articles']:
    if article['description'] is not None:
        content += article['title'] + '\n' + article['description'] + '\n\n'

content = content.encode('utf-8')
print(send_email(content))
