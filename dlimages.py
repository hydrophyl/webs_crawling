import requests
from bs4 import BeautifulSoup
import wget
import os

os.chdir('C:/Users/Admin/Documents/dlimages')
site = "https://boards.4chan.org/wg/thread/7550366"
response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('a', class_='fileThumb')
urls = [img['href'] for img in img_tags]
list_of_images = []

for url in urls:
    print(url)
    #print("http:" + url[:-5] + ".jpg")
    #url = "http:" + url[:-5] + ".png"
    list_of_images.append(url)

for i in range(0,len(list_of_images)):
    print(list_of_images[i])
    wget.download('http://' + list_of_images[i])
