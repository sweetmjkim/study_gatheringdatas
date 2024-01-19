# 데이터명 : 한국주택금융공사_전세자금대출 금리 정보
# from : https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15082033
import requests

# url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?serviceKey=GiqSMasfSR7XrTX2F5uIxIdKTvXYAXTPdcKpnBtPNDH9yBKpc9Hcv2%2BmzhTo6ra260JiX3a0IS1A5QDTBgrRoRw%3D%3D&pageNo=1&numOfRows=30&dataType=JSON'
url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'            # 사이트 주소(Call Back URL) // https: 에서 s는 삭제해야한다.

# serviceKey=GiqSMasfSR7XrTX2F5uIxIdKTvXYAXTPdcKpnBtPNDH9yBKpc9Hcv2%2BmzhTo6ra260JiX3a0IS1A5QDTBgrRoRw%3D%3D
# &pageNo=1
# &numOfRows=10
# &dataType=JSON
params = {'serviceKey' :'GiqSMasfSR7XrTX/5uIxIdKTvXYAXTPdcKpnBtPNDH9yBKpc9Hcv2+mzhTo6ra260JiX3a0IS1A5QDTBgrRoRw=='      # 공공데이터 포털에서 받은 인증키(Decoding)
          ,'pageNo' : 1                 # 페이지번호
          ,'numOfRows' : 10             # 한 페이지 결과 수
          ,'dataType' : 'JSON'}         # 데이터타입

# response = requests.get(url)
response = requests.get(url, params=params)

print(response.content)

import json
contents = json.loads(response.content)

type(contents)                          # 데이터 타입
# <class 'dict'>
contents['header']
# {'resultCode': '00', 'resultMsg': '정상'}
contents['header']['resultCode']
# '00'              00 이면 정상의미
contents['body']['totalCount']
# 18
type(contents['body']['items'])         # 리스트 정보의 데이터 타입
# <class 'list'>

# mongoDB 저장
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost:27017")              # mongodb에 접속 -> 자원에 대한 class
database = mongoClient["data_go_kr"]                                # database 연결
collection = database['rent-loan-rate-info_rate-list']              # collection 작업
result = collection.insert_many(contents['body']['items'])          # insert 작업 진행
pass