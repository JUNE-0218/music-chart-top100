import requests
from bs4 import BeautifulSoup

response = requests.get('https://music.bugs.co.kr/chart')
html = response.text    

soup = BeautifulSoup(html, 'html.parser') 


title1 = soup.find_all("p",{"class":"title"})
artist1 = soup.find_all("p",{"class":"artist"})
time = soup.find("p", {"class":"segmented"})
current = time.find("a").get_text()
time1 = soup.find("time")
time2 = time1.get("datetime")
print(current, "-", time2)

i = 0
b = 1

title = []
artist = []

for x in title1:
    title.append(x.find("a").get_text())

for d in artist1:
    artist.append(d.find("a").get_text())


while i <= 99:
    print(f"{b}위",title[i], "-", artist[i])
    i = i + 1
    b = b + 1
