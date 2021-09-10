# 抓取PTT電影版 html
# 教學 https://www.youtube.com/watch?v=9Z9xKWfNo7k&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=19

import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"

#模仿正常人的動作
#所以建立一個request1物件，附加 Reques header資訊
request1=req.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
})

with req.urlopen(request1) as response1: #req.urlopen(url)變成req.urlopen(request1)
    data1=response1.read().decode("utf-8")
# print(data1)

#用bs4解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data1,"html.parser") #html.parser意思用BeautifulSoup 來解析 HTML 的語法
# print(root.title.string) #測試網頁大標題抓取，抓取title的string
titles=root.find_all("div",class_="title") #find是找第一個，find_all找全部
# print(title1.a.string) #測試小標題抓取，抓取class=title 的 div中的a的string
for title in titles:
    if title.a != None:
        print(title.a.string)
