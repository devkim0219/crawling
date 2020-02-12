from bs4 import BeautifulSoup
import urllib.request, time, csv
import sqlite3

def get_list_records(table, list_records):
    for i, r in enumerate(table.find_all('tr')):
        for j, c in enumerate(r.find_all('td')):
            print(j, ':::', c)

            if j == 0:
                no = int(c.text.strip())
            
            elif j == 1:
                rate = str(c.find('em').text.strip())
                title = str(c.find('a', class_='movie').text.strip())
                review = str(c.text).split('\n')[5]

            elif j == 2:
                author = str(c.find('a', class_='author').text.strip())
                date = str(c.text).split('****')[1]

        try:
            record_t = tuple([no, rate, title, review, author, date])
            list_records.append(record_t)

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

conn = sqlite3.connect('./data/example.db')

with conn:
    c = conn.cursor()
    
    sql = 'create table if not exists movie (no integer, grade integer, title text, content text, writer text, date text)'
    c.execute(sql)
    conn.commit()
    
    sql = 'insert into movie values (?, ?, ?, ?, ?, ?)'
    c.executemany(sql, list_records)
    conn.commit()

    sql = 'select * from movie'
    c.execute(sql)

    rows = c.fetchall()

    for row in rows:
        print(row)