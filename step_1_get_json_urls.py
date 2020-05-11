import requests
from bs4 import BeautifulSoup
import json

url ='https://www.sylvanlearning.com/locations'

res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
# countries = soup.find('div','byCountry')
us = soup.find('div','unitedStates')
canada = soup.find('div','canada')
inter = soup.find('div','international')
branchs = [us,canada,inter]
urls = []
for br in branchs:
    branch = br.find('h2').text
    lis = br.findAll('li')
    for li in lis:
        link = f"https://www.sylvanlearning.com{li.find('a')['href']}".lower().replace(' ','%20').strip()
        location = li.find('a').text
        urls.append({"branch": branch, "location":location,"url":link})

with open('urls.json', 'w') as file:
    json.dump(urls, file)