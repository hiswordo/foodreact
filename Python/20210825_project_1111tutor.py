from modules.crawler import pageParser
import bs4

# 找尋20頁面，內有視訊教學內容的連結頁面
for num in range(1,21):
    data = pageParser("https://tutor.1111.com.tw/case/CaseSearch.asp?page="+str(num)+"&newSearch=search&Item1=2&sDuty0=100101,100103")
    titles = data.find_all("span",class_="mobiContent")

    newlinkList = []
    for title in titles:
        if title.a != None:
            if (title.a["href"]).find("Detail") > 0:
                data2 = pageParser("https://tutor.1111.com.tw/"+title.a["href"])
                titles2 = data2.find_all("span",class_="col")
                for title2 in titles2:
                    if title2.string=="視訊教學":
                        newlinkList.append("https://tutor.1111.com.tw/"+title.a["href"])

    for newlink in newlinkList:
        print(newlink)

# 應徵頁面
""" from modules.crawler import pageParser
data = pageParser("https://tutor.1111.com.tw/case/caseDetail.asp?CNo=8647421668152430840670261027068228841571978449")
titles = data.find_all("span",class_="col")
for title in titles:
    if title.string=="視訊試教"
 """

# 搜尋葉面
""" from modules.crawler import pageParser
data = pageParser("https://tutor.1111.com.tw/case/CaseSearch.asp?page=1&newSearch=search&Item1=2&sDuty0=100101,100103")
titlesSub = data.find_all("span",class_="col-md-35")
titlesGrade = data.find_all("span",class_="col-md-2")
for title in titlesSub:
    print(title.) """