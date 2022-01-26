import requests
from bs4 import BeautifulSoup
import json


def yamuparser():
    URL = input('Вставь ссылку на плейлист ')
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')
    rawdata = soup.body.script.string

    notsorawdata = rawdata[7:-1]  # Поискать более элегантный способ избавиться от var Mu= ... ;

    data = json.loads(notsorawdata)

    pageDataKEY = data.get('pageData')
    playlistKEY = pageDataKEY.get('playlist')
    tracksKEY = playlistKEY.get('tracks')

    playlist = ''

    for item in tracksKEY:
        playlist += item.get('title')
        playlist += ' '
        temp = item.get('artists')
        temp1 = temp[0]
        playlist += temp1.get('name')
        playlist += '\n'

    print(playlist)

yamuparser()
