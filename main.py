from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"

response = requests.get(url)

data = response.text

print(data)
