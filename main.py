import requests
import json

METHOD = 'photos.get'
TOKEN = input('Введите токен\n')
V = '5.131'
id = input('Введите ваш id:\n')
YA_Token = input('Введите токен яндекса:\n')
url_vk = 'https://api.vk.com/method/'+METHOD+'?PARAMS&access_token='+TOKEN+'&v='+V
params_vk = {'owner_id' : id, 'album_id' : 'profile', 'extended' : '1'}
url_ya = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {"Authorization": YA_Token}

def photo_link():
    res = requests.get(url=url_vk, params=params_vk)
    response = res.json()['response']['items']
    # print(response)
    for a in response:
        size = a['sizes'][-1]['type']
        likes = a['likes']['count']
        download_url = a['sizes'][-1]['url']
        params_ya = {'path': likes, 'overwrite': 'true', 'url': download_url}
        resp = requests.post(url=url_ya, headers=headers, params=params_ya)
        print(resp.json())


        json_file = {}
        json_file['filename'] = likes
        json_file['size'] = size
        with open('final.json', 'w') as file:
            json.dump(json_file,file)

print(photo_link())


fields = 'id,media_url'
access_token = input('Введите долгосрочный токен:\n')
media_id = input('Введите user_id\n')
url_insta = 'https://graph.instagram.com/me/media?fields='+fields+'&access_token='+access_token

def photo_link_insta():
    res = requests.get(url=url_insta)
    response = res.json()['data']
    # print(res.json())
    for media in response:
        download_url = media['media_url']
        name = media['id']
        params_insta = {'path': name, 'overwrite': 'true', 'url': download_url}
        resp = requests.post(url=url_ya, headers=headers, params=params_insta)
        print(resp.json())

print(photo_link_insta())
