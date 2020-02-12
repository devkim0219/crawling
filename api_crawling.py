import requests

client_id = 'tn_wFE6aIrraSygS4kxH'
client_secret = 'uKZwI0FfKT'

naver_open_api = 'https://openapi.naver.com/v1/search/news.json?query=KBO'
header_params = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
res = requests.get(naver_open_api, headers=header_params)

if res.status_code == 200:
    data = res.json()

    for index, item in enumerate(data['items']):
        print(index + 1, item['title'].replace('&quot;', ''), item['link'])
    
else:
    print('Error Code: ', res.status_code)