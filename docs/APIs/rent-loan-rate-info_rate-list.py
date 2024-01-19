# 데이터명 : 한국주택금융공사_전세자금대출 금리 정보
# from : https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15082033
import requests

# url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?serviceKey=GiqSMasfSR7XrTX2F5uIxIdKTvXYAXTPdcKpnBtPNDH9yBKpc9Hcv2%2BmzhTo6ra260JiX3a0IS1A5QDTBgrRoRw%3D%3D&pageNo=1&numOfRows=30&dataType=JSON'
url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

# serviceKey=GiqSMasfSR7XrTX2F5uIxIdKTvXYAXTPdcKpnBtPNDH9yBKpc9Hcv2%2BmzhTo6ra260JiX3a0IS1A5QDTBgrRoRw%3D%3D
# &pageNo=1
# &numOfRows=10
# &dataType=JSON
params = {'serviceKey' :'GiqSMasfSR7XrTX2F5uIxIdKTvXYAXTPdcKpnBtPNDH9yBKpc9Hcv2%2BmzhTo6ra260JiX3a0IS1A5QDTBgrRoRw%3D%3D'
          ,'pageNo' : 1
          ,'numOfRows' : 10
          ,'dataType' : 'JSON'}

# response = requests.get(url)
response = requests.get(url, params=params)

print(response.content)

pass