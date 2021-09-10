# 抓取八卦電影版 html
# 教學 https://www.youtube.com/watch?v=BEA7F9ExiPY&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=20

# Step1. Request with url and headers
import urllib.request as req
def getData(url):
    request1=req.Request(url,headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
    })
    # Step2. Read and decode the Response
    with req.urlopen(request1) as response1:
        data1=response1.read().decode("utf-8")

    # Step3. Parser the ingredients with bs4
    import bs4
    root=bs4.BeautifulSoup(data1,"html.parser") 

    # Step4. Making the soup u wants to eat
    titles=root.find_all("div",class_="title") 
    for title in titles:
        if title.a != None:
            print(title.a.string)

    # 提取上一頁的連結
    nextLink = root.find("a",string="‹ 上頁")  #如果用find_all即使只找到一個也會得到[List]
    return nextLink["href"] #直接就抓到a的href屬性的內容 並還給這個函式

pageLink="https://www.ptt.cc/bbs/Gossiping/index.html"
# getData(pageLink) #呼叫函數等同原本
count = 0
pagesWant = 3
while count < pagesWant:
    pageLink = "https://www.ptt.cc" + getData(pageLink)
    count += 1
