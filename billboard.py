import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.billboard.com/charts/hot-100')
html = response.text    


soup = BeautifulSoup(html, 'html.parser') 

week = soup.find("h2", {"id":"section-heading"}).text.strip()

rank = soup.find_all("div",{"class":"o-chart-results-list-row-container"})

i = 1

print(week)
for info in rank:
    title = info.find("h3").text.strip()
    singer = info.find("h3").find_next('span').text.strip()
    print(f"{i}위 {title} - {singer}")
    i = i + 1