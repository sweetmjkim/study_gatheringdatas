import requests

url = 'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'

params = {'serviceKey' : 'GiqSMasfSR7XrTX/5uIxIdKTvXYAXTPdcKpnBtPNDH9yBKpc9Hcv2+mzhTo6ra260JiX3a0IS1A5QDTBgrRoRw=='
          ,'pageNo' : 1
          ,'numOfRows' : 10
          ,'type' : 'json'
          ,'bidNtceBgnDt' : 201712010000
          ,'bidNtceEndDt' : 201712312359}

response = requests.get(url, params=params)

print(response.content)

import json
contents = json.loads(response.content)
pass

# mongodb 저장
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost:27017")              # mongodb에 접속 -> 자원에 대한 class
database = mongoClient["data_go_kr"]                                # database 연결
collection = database['PubDataOpnStdService']              # collection 작업
result = collection.insert_many(contents['response']['body']['items'])
pass
