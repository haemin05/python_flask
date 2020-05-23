import os
import sys
import requests
client_id = "여기를 지우고 클라이언트 아이디를 붙여넣으세요."
client_secret = "여기를 지우고 클아이언트 시크릿을 붙여넣으세요."

url = "https://openapi.naver.com/v1/vision/celebrity"

files = {'image': open('여기를 지우고 파일 이름(확정자 포함)을 붙여넣으세요', 'rb')}
headers = {'X-naver-Client-Id': client_id, 'X-naver-Client-Secret': client_secret}
response = requests.post(url, files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print(response.text)
else:
    print('Error Code:' + rescode)