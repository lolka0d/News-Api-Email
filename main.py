import requests
import os

api_key = os.getenv("API_KEY")
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-19&sortBy=publishedAt&apiKey=" + api_key

req = requests.get(url)
responce = req.json()

for article in responce['articles']:
    print(article['title'])
    print(article['description'])