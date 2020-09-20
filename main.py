# encoding=utf8
import requests
from bs4 import BeautifulSoup
import json
import webbrowser
from wox import Wox

udid = 'a4684a67c5db66436da276d582163766f927d703'
api_key = '054022eaeae0b00e0fc068c0c0a2102a'


class Main(Wox):
    def query(self, query):
        if not query:
            return ""
        r = requests.get(
            'https://douban.lovemefan.top/api/v2/search/movie?channel=Douban&udid='
            + udid + '&apikey=' + api_key + '&q=' + query,
            params={'start': 0})

        r_json = r.json()
        results = []
        for item in r_json['items']:
            res = {}
            title = item['target']['title']
            sub_title = item['target']['card_subtitle']
            # year = item['target']['year']
            movie_id = item['target']['id']
            open_url = 'https://movie.douban.com/subject/' + movie_id
            res["Title"] = title
            res["SubTitle"] = sub_title
            res["IcoPath"] = "Images\\movies.png"
            res["JsonRPCAction"] = {
                "method": "openUrl",
                "parameters": [open_url]
            }
            results.append(res)
        return results

    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Main()
