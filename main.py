import requests
from googleapiclient.http import MediaFileUpload
from Google import Create_service

secret_file = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive/']

service = Create_service(secret_file, API_NAME, API_VERSION, SCOPES)



METHOD = 'photos.get'
TOKEN = input('Введите токен:\n')
V = '5.131'
id = input('Введите id пользователя:\n')
url_vk = 'https://api.vk.com/method/'+METHOD+'?PARAMS&access_token='+TOKEN+'&v='+V
params_vk = {'owner_id' : id, 'album_id' : 'profile', 'extended' : '1'}
url_ya = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {"Authorization": "AQAAAAAgsrE-AADLW8se8WiLSEWUhO9H3-tfWZM"}
headers_google = {"Authorization": "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"}
url_google = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=media'

#oauth google 593144244514-k0mub33ahqo1f4f58ol1gr2m5rf26frc.apps.googleusercontent.com
#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

# Google dz-netology 593144244514
# drive-api@dz-netology.iam.gserviceaccount.com
# 105146919918360586871
# 150421694
# 89649cef89649cef89649cefc9891dc1258896489649cefe820d12a2a7204186f074e23
#key = AIzaSyAhZduSivLeo0KK8PFg-8UubZLOZHJmC-E

def photo_link():
    res = requests.get(url=url_vk, params=params_vk)
    response = res.json()['response']['items']
    print(response)
    for a in response:
        likes = a['likes']['count']
        download_url = a['sizes'][-1]['url']
        params_ya = {'path': likes, 'overwrite': 'true', 'url': download_url}
        # resp = requests.post(url=url_ya, headers=headers, params=params_ya)
        # print(resp.json())
        mime_types = ['image/jpeg']
        file_metadata = {'name' : likes}





print(photo_link())

