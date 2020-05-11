import requests, json
from bs4 import BeautifulSoup

class open_json:
    with open('urls.json', 'r') as file:
        data = file.read()
    datas = json.loads(data)

class hitung:
    hitung =0

data = []
for d in open_json.datas:
    hitung.hitung += 1
    if hitung.hitung == 2:
        break
    branch = d['branch']
    location = d['location']
    url = d['url']
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    area = soup.findAll('div',{'itemtype':'http://schema.org/LocalBusiness'})
    for a in area:
        location_name = a.find('h2').text.strip()
        address = a.find('span',{'itemprop':'address'})
        streetAddress = address.find('span',{'itemprop':'streetAddress'}).text.strip()
        stes = address.text
        if 'Ste' in stes:
            ste = stes.split('\n')[2].strip()
        else:
            ste = ''
        locality = address.find('span',{'itemprop':'addressLocality'}).text.strip()
        region = address.find('span',{'itemprop':'addressRegion'}).text.strip()
        postal_code = address.find('span',{'itemprop':'postalCode'}).text.strip()
        telp = a.find('span',{'itemprop':'telephone'}).text.strip()
        web_sc = a.find('a',{'itemprop':'url'})['href']
        # print(web_sc)
        # print(telp)
        # print(postal_code)
        # print(region)
        # print(locality)
        # print(ste)
        # print(streetAddress)
        # print(location_name)
        print(branch)
        print(location)
        json_data_list = {
            'Title':location,
            'Branch':branch,
            'Location Name':location_name,
            'Street Address':streetAddress,
            'Ste':ste,
            'Locality':locality,
            'Region':region,
            'Postal Code':postal_code,
            'Telp':telp,
            'Website & Schedules URL':web_sc}
        #append json data to data
        data.append(json_data_list)

with open('data.json', 'w') as file:
    json.dump(data, file)