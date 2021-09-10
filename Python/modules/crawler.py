# 001pageParser
import urllib.request as req
from bs4 import BeautifulSoup as bs
from urllib.parse import quote

# 002.
import requests
import json

# 001.pageParser: 使用者身分request，開啟網頁得到response，放到bs4裡面用html解析
def pageParser(url, keyword=""):
    key = quote(keyword)
    url = url + key
    request = req.Request(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
        },
    )
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs(data, "html.parser")
    return root


# 002.分析json資料的網址 (並刪除pretext，google maps評論專用?)
def jsonParser(url):
    text = requests.get(url).text
    pretext = ")]}\'" # 取代掉特殊字元，這個字元是為了資訊安全而設定的喔。
    text = text.replace(pretext,'')
    # return text
    soup = json.loads(text) #把字串讀取成json #! losds 有s喔
    return soup