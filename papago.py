import requests

client_id = 'tn_wFE6aIrraSygS4kxH'
client_secret = 'uKZwI0FfKT'

text = input('번역할 내용을 입력하세요: ')

naver_open_api = 'https://openapi.naver.com/v1/papago/n2mt?source=ko&target=en&text=' + text
header_params = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
res = requests.get(naver_open_api, headers=header_params)

if res.status_code == 200:
    data = res.json()
    print(data)

else:
    print('Error Code: ', res.status_code)