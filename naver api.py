import os
import sys
import requests
client_id = 'jIohkW8D0kKgmyzwzDlo'
client_secret = 'PGqWEGZseE'
#url = 'https://openapi.naver.com/v1/vision/face'
url = 'https://openapi.naver.com/v1/vision/celebrity'
files = {'image': open('files name', 'rb')}
headers = {'X-naver-Client-Id': client_id, 'X-naver-Client-Secret': client_secret }
response = requests.post(url, files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print(response.text)
else:
    print('Error Code:' + rescode)