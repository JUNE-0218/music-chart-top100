import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
response = requests.get('https://www.melon.com/chart/index.htm',headers=header)
html = response.text



soup = BeautifulSoup(html, 'html.parser') 

time = soup.find("span",{"class":"year"}).get_text()
hour = soup.find("span", {"class": "hour"}).get_text()
print(time, hour)

song = soup.find_all("div", {"class": f"ellipsis rank01"})
singr = soup.find_all("div", {"class": f"ellipsis rank02"})

title = []
singer = []

for i in song:
    title.append(i.find('a').text)

for j in singr:
    singer.append(j.find('a').text)
a = 0
b = 1



while a <= 99:
    print(f"{b}위",title[a], "-", singer[a])
    a = a + 1
    b = b + 1
