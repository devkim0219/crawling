import requests

service_key = 'S4%2BrnIaFzwO%2BIkbQSrqhLgvwu8BUZBB8xnoZCLd4CwllAfw5i392rLCAkRK1%2FjA3N7PcXmjEY49unAkHLbo1bQ%3D%3D'

open_api = f'http://apis.data.go.kr/6260000/BusanPopulationStaticService/getPopulationInfo?serviceKey={service_key}&numOfRows=5&pageNo=1&resultType=json'

res = requests.get(open_api)

print(res.content)

# 파일로 저장
# f = open('./data/open_api.json', 'wb')
# f.write(res.content)
# f.close()