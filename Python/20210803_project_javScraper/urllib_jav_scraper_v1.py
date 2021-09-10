javnum = "MKON-054"
pageLink="https://javdb.com/search?q="+ javnum +"&f=all"

# Step1. Request with url and headers
import urllib.request as req
request1=req.Request(pageLink,headers={
    # "cookie":"over18=1",
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
})
# Step2. Read and decode the Response
with req.urlopen(request1) as response1:
    data1=response1.read().decode("utf-8")

import bs4
root1=bs4.BeautifulSoup(data1,"html.parser") 

fNextLink = root1.find("a",class_="box")

nextLink = "https://javdb.com/"+fNextLink["href"]

request2=req.Request(nextLink,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
})
with req.urlopen(request2) as response2:
    data2=response2.read().decode("utf-8")
root2=bs4.BeautifulSoup(data2,"html.parser") 
titles=root2.find_all("div",class_="panel-block")

# if titles_name.replace("<strong>","").replace("</strong>","")=="日期:":
#     print("right")
# else:
#     print("wrong")
# print(titles_name.replace("<strong>","").replace("</strong>",""))
for title in titles:
    title_ckname=str(title.find_next().text) # 本來多此一舉耶 replace("<strong>","").replace("</strong>","")
    content=str(title.find_next().find_next().text)
    if title_ckname=="番號:":
        print("<id>"+content+"</id>")
    elif title_ckname=="日期:":
        print("<releasedate>"+content+"</releasedate>")
    elif title_ckname=="時長:":
        print("<runtime>"+content.replace(" 分鍾","")+"</runtime>")
    elif title_ckname=="片商:":
        print("<studio>"+content+"</studio>")
    elif title_ckname=="系列:":
        print("<set>"+content+"</set>")
    elif title_ckname=="評分:":
        pointPosition=content.index("分")
        print("<rating>"+content[1:pointPosition]+"</rating>")
    elif title_ckname=="演員:": #很多人就麻煩了
        actorPosition=content.index("♀")
        print("<actor>\n"+"  <name>"+content[1:actorPosition]+"</name>"+"\n  <thumb></thumb>\n</actor>")
    elif title_ckname=="導演:":
        print("<director>"+content+"</director>")        
    elif title_ckname=="類別:":
        contentlist=list(content.replace(",","").split()) #.split()可以將空格分開，str轉list就完美
        for j in contentlist:
            print("<genre>"+j+"</genre>")
        # print(contentlist)
        # print("<genre>"+content.replace(", "," \ n ")+"</genre>") # replace with \n 根本做不到...原因不明??




# checkname=[]
# checkname.append=titles[0].find_next()
# print(checkname[0])
# for title in titles
#     title=str(title.find_next()) #所以指定的title[1]是bs4.element.Ta的NoneType，不能做字串變動
#     titles_ckname=titles_name.replace("<strong>","").replace("</strong>","")
#     if titles_ckname =="番號:":
#         print(titles[i].span.text)
#     else:
#         print("fail")

# title01=titles.find("strong",string="番號")

# print(titles[0].strong.text)
# for title in titles:
#     print(title.text)

# pageLink = "https://javdb.com/" + getData(pageLink)
# print(pageLink)
# pageLink = "https://javdb.com/" + getData(pageLink)
# print(pageLink)
    # pageLink = "https://www.ptt.cc" + getData(pageLink)
