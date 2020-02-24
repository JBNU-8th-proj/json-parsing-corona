import urllib.request
import json

corona_address = "https://api.coronas.info/patients/"

req = urllib.request.urlopen(corona_address)
res = req.readline()

j = json.loads(res)

for i in j:
    print(i['id'], '님은 ', i['status'], '상태이며 ', '감염이유는 ', i['infected_route'], '로 추정되고 ', i['country'], '사람입니다.', sep='')

    # 이동경로가 있지 않은 데이터도 있으므로 예외처리
    try:
        print('마지막 이동경로는', i['last_movement']['lat'], '의 위도와', i['last_movement']['lng'], '의 경도로 추정됩니다')
    except:
        print('마지막 이동경로의 데이터가 존재하지 않습니다')

    # 정확한 데이터만 집어넣고 싶다면 print(i['id']~ 예외처리를 시키면 됨)