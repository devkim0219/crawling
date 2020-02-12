from bs4 import BeautifulSoup
import urllib.request, time

url = 'https://music.bugs.co.kr/chart'

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')

table_list = soup.select('#CHARTrealtime > table > tbody')

for row in table_list:
    for rank in row.select('div.ranking > strong'):
        print(rank.text)

    for title in row.select('p.title'):
        print(title.text)