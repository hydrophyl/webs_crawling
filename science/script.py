import requests
from bs4 import BeautifulSoup

url = "view-source:https://www.reddit.com/"
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

print(soup.prettify())
