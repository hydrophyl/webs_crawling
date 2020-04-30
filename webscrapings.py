import requests
url = "https://www.sciencedaily.com/releases/2020/04/200428223728.htm"
page = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

list_of_p = []
title = soup.find("h1")
print(title)

for p in soup.find_all("p"):
    text = p.text
    print(text)
    print()
    list_of_p.append(text)

print(list_of_p)
import csv

csv_file = open('output.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['title', 'pararaphs'])
for items in list_of_p:
    writer.writerow([title,items])

csv_file.close()
