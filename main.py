from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"

response = requests.get(url)

print(response)
