from bs4 import BeautifulSoup
import urllib.request, time, json

def get_list_records(table, list_records):
    for i, r in enumerate(table.find_all('tr')):
        for j, c in enumerate(r.find_all('td')):
            print(j, ':::', c)

            if j == 0:
                record = {'번호': int(c.text.strip())}
            
            elif j == 1:
                record.update({'평점': str(c.find('em').text.strip())})
                record.update({'영화': str(c.find('a', class_='movie').text.strip())})
                record.update({'140자평': str(c.text).split('\n')[5]})
            
            elif j == 2:
                record.update({'글쓴이': str(c.find('a', class_='author').text.strip())})
                record.update({'날짜': str(c.text).split('****')[1]})

        try:
            list_records.append(record)

        except:
            pass

    return(list_records)

# params = urllib.parse.urlencode({'page': 1})
# url = 'https://movie.naver.com/movie/point/af/list.nhn?&%s' %params
# response = urllib.request.urlopen(url)
# navigator = BeautifulSoup(response, 'html.parser')

# table = navigator.find('table', class_='list_netizen')

list_records = []
page = 1

while True:
    params = urllib.parse.urlencode({'page': page})
    url = 'https://movie.naver.com/movie/point/af/list.nhn?&%s' %params 
    response = urllib.request.urlopen(url)
    navigator = BeautifulSoup(response, 'html.parser')
    table = navigator.find('table', class_='list_netizen')
    page += 1

    # if response.getcode == 200:
    if page != 5:
        list_records = get_list_records(table, list_records)

    else:
        break

with open('./data/naver_movie.json', 'wb', encoding='UTF-8') as f:
    json.dump(list_records,f, sort_keys=True)