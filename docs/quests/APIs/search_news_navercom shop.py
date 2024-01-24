# from : https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md#%EC%87%BC%ED%95%91

import requests         #postman app 역할

# request API 요청
url = 'https://openapi.naver.com/v1/search/shop'                # uri 주소
params = {'query' : '블랙박스'}                                  # 검색어 : 블랙박스
headers = {'X-Naver-Client-Id' : 'JpVPHqeIjR0_FhfaGShS'         # api인증키
           ,'X-Naver-Client-Secret' : 'rWFwXYlaa5'}

response = requests.get(url, params=params, headers=headers)

# response API 응답
response.content

# json을 변수로 변환
import json
contents = json.loads(response.content)

from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost:27017")              # mongodb에 접속 -> 자원에 대한 class
database = mongoClient["data_go_kr"]                                # database 연결
collection = database['search_shop_info']                           # collection 작업
collection1 = database['search_shop_list']                           # collection 작업
pass

info = {
    "lastBuildDate" : contents['lastBuildDate']
    ,"total" : contents['total']
    ,"start" : contents['start']
    ,"display" : contents['display']
    }
result_info = collection.insert_one(info)      # insert 작업 진행
pass

id_relative = result_info.inserted_id

for i in contents['items'] : 
    i['id_relative'] = id_relative
collection1.insert_many(contents['items'])
pass
