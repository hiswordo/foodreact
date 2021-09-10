# javnum = "MAAN-6801"

import urllib.request as req
import bs4
# 網址encode
import urllib.parse
# 存圖片
import requests
import shutil 
# 切割圖片
import cv2
# 處理資料
import os
import shutil
import win32con, win32api
# 篩選部分文字
import re

#搜尋資料夾內影片檔的檔名，並刪減成番號名稱
files = os.listdir() #['#cat', '123.txt']
for inName in files:
    tmp = os.path.splitext(inName)  #('#cat', '') ('123', '.txt')
    if tmp[1] == '.mp4' or tmp[1] == '.ts':
        # print(tmp[1])
        javnum = re.search(r'[a-z][a-z0-9]{0,}-[0-9]{2,}',str(tmp[0]),re.I)[0]
        # javnum = tmp[0]
        videoname = tmp[0]+tmp[1]
        videotype = tmp[1]
        break
# print(javnum)
# print(videoname)

# # #複製有縮圖的資料夾，並重新命名，再創建隱形資料夾
if not os.path.exists("BridgeName"):
    shutil.copytree('G:\Coverbase01','BridgeName') 
if not os.path.exists(javnum):
    os.rename("BridgeName", javnum)
if not os.path.exists(javnum+"/.actors"):
    os.mkdir(javnum+"/.actors")
win32api.SetFileAttributes(javnum+'/desktop.ini', 2)
win32api.SetFileAttributes(javnum+'/.actors', 2)
# # os.mkdir(javnum)  #已存在就無法建立

#將影片移動到資料夾內
if os.path.exists(videoname):
    destination = javnum+"/"+videoname
    shutil.move(videoname,destination) #可以設定如果有影片

#bs4分析頁面的function
def pageParser(url):
    request1=req.Request(url,headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
    })
    with req.urlopen(request1) as response1:
        data1=response1.read().decode("utf-8")
    root1=bs4.BeautifulSoup(data1,"html.parser") 
    return root1
# print(pageParser(pageLink)) #分析結果html

# 搜尋結果的頁面分析
pageLink="https://javdb.com/search?q="+ javnum +"&f=all"
idSearchPage = pageParser(pageLink)

fNextLink = idSearchPage.find("a",class_="box") #搜尋結果的第一個連結 = 真正要連結
nextLink = "https://javdb.com/"+fNextLink["href"]

# 番號頁面分析
idPage = pageParser(nextLink)

# # function下載圖片
def picDown(url,picName):
    res = requests.get(url, stream=True)
    pic = open(picName,'wb') 
    shutil.copyfileobj(res.raw,pic)
    pic.close() 
    del res

# # function維持圖片比例縮放
# def image_resize(image, width = None, height = None, inter = cv2.INTER_CUBIC):
#     dim = None
#     (h, w) = image.shape[:2]

#     if width is None and height is None:
#         return image
#     if width is None:
#         r = height / float(h)
#         dim = (int(w * r), height)
#     else:
#         r = width / float(w)
#         dim = (width, int(h * r))
#     resized = cv2.resize(image, dim, interpolation = inter)
#     return resized

# 獲取橫幅封面圖，儲存fanart圖片檔
# 沒有gallery的會出錯，所以只有封面的頁面判斷，獲取不同的fanart網址
fanartonlyPicCK = idPage.find('a',class_="cover-container")
if fanartonlyPicCK != None:
    fanartPicLink = idPage.find('a',class_="cover-container").find_next()["src"]
else:
    fanartPicLink = idPage.find('a',attrs={'data-fancybox':'gallery'})["href"] #第一個即是fanart，所以不用find_all
#下載fanart.jpg
picDown(fanartPicLink,javnum+"/fanart.jpg")
# 製作poster
# 切割圖片(不同的fanart切法不同):377x538/379x536
img = cv2.imread(javnum+"/fanart.jpg")
crop_img = img[0:579, 421:800]  # [y座標，X座標]
cv2.imwrite(javnum+'/poster.jpg', crop_img)
shutil.copyfile(javnum+'/poster.jpg', javnum+'/folder.jpg')

# # 放大圖片:166x236 -> 380x540.241
# # 獲取封面圖連結，下載封面圖，放大後，效果奇差!
# imgPosterLink = idSearchPage.find("div",class_="item-image").find_next()["data-src"] # imgPoster = idSearchPage.find("img",class_="yall-loaded")為啥不行??
# picDown(imgPosterLink,javnum+"/poster_small.jpg")
# img_small = cv2.imread(javnum+'/poster_small.jpg')
# imgEnlarge = image_resize(img_small, height = 538) 
# # cv2.imshow('Result', imgEnlarge)
# # cv2.waitKey(0)
# cv2.imwrite(javnum+'/poster_small.jpg', imgEnlarge)

# 製作nfo影片標籤檔案 #actor original
nfoContent = []
nfoContent.append('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n<movie>')
# original title
h2title = str(idPage.find("h2").text)
posTitle = h2title.index(" ")
h2titlermNum = h2title[posTitle+1:-1]
nfoContent.append("  <title></title>")
#導入trailer影片，popup影片上面的網址也會跟著改變，但有的官方網站只能日本才能進
#同上，沒有gallery的問題
if fanartonlyPicCK != None:
    trailerVideoLink = ""
else:
    trailerPageLink = nextLink+"#gallery-2"
    trailerPage = pageParser(trailerPageLink)
    # trailerVideoLink = str(trailerPage.find("video",id="preview-video").find_next()["src"])
    trailerVideoLink = trailerPage.find("video",id="preview-video").find_next()["src"]
    if trailerVideoLink=="":
        print("抓poster摟")
        imgPosterBigLink = trailerPage.find("div",class_="preview-images").find_next().find_next_sibling()["href"]
        picDown(imgPosterBigLink,javnum+"/poster_big.jpg")
    else:
    #如果有video，一種是雙斜線，另一種是外連
        if trailerVideoLink.index("//")==0:
            nfoContent.append("  <trailer>"+trailerVideoLink[2:]+"</trailer>")
        nfoContent.append("  <trailer>"+trailerVideoLink+"</trailer>")
nfoContent.append("  <plot></plot>")
nfoContent.append("  <thumb>"+fanartPicLink+"</thumb>\n"+"  <fanart>\n"+"    <thumb>"+fanartPicLink+"</thumb>\n"+"  </fanart>")
titles = idPage.find_all("div",class_="panel-block")
for title in titles:
    title_ckname=str(title.find_next().text) # 本來多此一舉耶 replace("<strong>","").replace("</strong>","")
    content=str(title.find_next().find_next().text) # 都要先從bs4 html轉成字串才可以做字串操作 #find_next()找到下一層的span"演員:"，再次find_next()下一層找到內文
    if title_ckname=="番號:":
        nfoContent.append("  <id>"+content+"</id>")
    elif title_ckname=="日期:":
        nfoContent.append("  <releasedate>"+content+"</releasedate>")
        content_year=content[0:4]
        nfoContent.append("  <year>"+content_year+"</year>")
    elif title_ckname=="時長:":
        nfoContent.append("  <runtime>"+content.replace(" 分鍾","")+"</runtime>")
    elif title_ckname=="片商:":
        nfoContent.append("  <studio>"+content+"</studio>")
    elif title_ckname=="系列:":
        nfoContent.append("  <set>"+content+"</set>")
    elif title_ckname=="評分:":
        pointPosition=content.index("分")
        nfoContent.append("  <rating>"+content[1:pointPosition]+"</rating>")
        voterPositionI=content.index("由")
        voterPositionF=content.index("人")
        nfoContent.append("  <votes>"+content[voterPositionI+1:voterPositionF]+"</votes>")
    elif title_ckname=="演員:":
        # 素人女優 [LUXU][SIRO][GANA][MAAN][NTK][JAC][EVA][SCUTE] [HGP][KNTR][MASS]
        comparNums = ["LUXU", "SIRO", "GANA", "MAAN", "NTK", "EVA", "SCUTE", "HGP", "KNTR", "MASS"] #"JAC"目前不用
        for comparNum in comparNums:
            checkJavN = javnum.upper().find(comparNum)
            if checkJavN != -1:
                # av-wiki用番號搜尋，取得女優name
                avwikiPageLink = "https://av-wiki.net/?s="+javnum+"&post_type=product"
                avwikiSearchPage = pageParser(avwikiPageLink)
                avStarName = avwikiSearchPage.find("p",class_="actress-name").find_next().text
                # 如果av-wiki也沒搜尋到女優
                if avStarName != "(≥o≤)":
                    avwikiAvStarLink = avwikiSearchPage.find("p",class_="actress-name").find_next().find_next()["href"] #備用
                    # javdb用name搜尋，取得女優pic
                    jpwdEncode = urllib.parse.quote(avStarName,safe='中村')
                    javdbAvStarPageLink = "https://javdb.com/search?f=actor&q="+jpwdEncode
                    javdbAvStarPage = pageParser(javdbAvStarPageLink)
                    javdbAvStardiv = javdbAvStarPage.find("span",class_="avatar")["style"] #已經取出成純文字，python就會認定成str 
                    avStarPicLink = re.findall("\((.+?)\)",javdbAvStardiv)[0]  #篩選()的網址
                    break
                else:
                    print("sorrry,bro, can't find")
                    avStarName="Unknown"
                    avStarPicLink=""
                    # 補完original標題
                    h2titleFnl = h2titlermNum
                    nfoContent.append("  <originaltitle>"+h2titleFnl+"</originaltitle>")
                    break
            else:
                #如果沒有女優，不用搜索javdb
                testerror=content.find("♀")
                if content.find("♀") == -1:
                    print("no avstar") #像這樣檢查六次素人，可以用break讓他出去for迴圈，但感覺不是最好的寫法
                    avStarName="Unknown"
                    avStarPicLink=""
                    # 補完original標題
                    h2titleFnl = h2titlermNum
                    nfoContent.append("  <originaltitle>"+h2titleFnl+"</originaltitle>")
                    break
                else:
                    # 在db列表上抓取第一個女優名稱，並連結頁面抓取圖片
                    actorPosition=content.index("♀")
                    avstarlink=title.find_next().find_next().find("a")["href"]
                    avStarName = content[1:actorPosition]
                    # 補完original標題，去掉女優名稱
                    h2titleFnl = h2titlermNum.replace(avStarName,"")
                    nfoContent.append("  <originaltitle>"+h2titleFnl+"</originaltitle>")
                    # 女優頁面分析 (如果沒有女優則跳過)
                    # 也可以從這邊載https://www.javbus.com/searchstar/ #哪裡有問題?
                    avStarPage = pageParser("https://javdb.com/"+avstarlink)
                    # 如果沒有女優圖片，不用搜索
                    if avStarPage.find("span",class_="avatar")!= None:
                        avStarPic = avStarPage.find("span",class_="avatar")["style"]# background-image: url(https://jdbimgs.com/avatars/nj/NJnx.jpg) 或者 None
                        avStarUrlini = str(avStarPic).index("url") # 指的是url的開頭，如上一行，開頭為18
                        avStarUrlfnl = str(avStarPic).index("jpg")
                        avStarPicLink = avStarPic[(avStarUrlini+4):(avStarUrlfnl+3)]
                        # 儲存女優頭貼圖片
                        picDown(avStarPicLink,javnum+"/.actors/"+avStarName+".jpg")
                        break
                    else:
                        avStarPicLink = ""
                        break
        nfoContent.append("  <actor>\n"+"    <name>"+avStarName+"</name>"+"\n    <thumb>"+avStarPicLink+"</thumb>\n  </actor>")
    elif title_ckname=="導演:":
        nfoContent.append("  <director>"+content+"</director>")        
    elif title_ckname=="類別:":
        contentlist=list(content.replace(",","").split()) #.split()可以將空格分開，str轉list就完美
        for j in contentlist:
            nfoContent.append("  <genre>"+j+"</genre>")

nfoContent.append("</movie>")

# #刪除標題太長的部分
# manytime = h2titleCK.find(" ")
# nextword = h2titleCK
# for i in range(manytime):
#     if len(nextword) > 50 : #保留50以內的文字，並斷在空白處
#         spacePos = nextword.rindex(" ")
#         nextword = h2titleCK[0:spacePos]
#     else:
#         finaltitle = nextword

def shrinkSenten(wordtest,num):
    lenSentence = num
    syntaxPos = []
    syntaxWd = [' ','！','…','】']
    for i in range(len(wordtest)):
        for k in syntaxWd:
            if wordtest[i]==k:
                syntaxPos.append(i)
                break
    # print(syntaxPos)
    syntaxPos.reverse() #從最後的符號跑到最前面
    for j in syntaxPos:
        if j < lenSentence-1:
            if wordtest[j]==" ":
                finalWord = wordtest[0:j] #最終字串，刪除空白
                return finalWord
            else:
                finalWord = wordtest[0:j+1] #最終字串，保留符號本身
                return finalWord
    # print(finalWord)

# 將nfo的片段，集合寫在一起
# print(h2titleFnl) #\nNA-001 natural☆girls \n 這樣無法創建檔案名稱

originalName_title = javnum+"_"+avStarName+" - "+shrinkSenten(str(h2titleFnl),80)+"("+content_year+")"
# 刪除windos非法字元
nfoFileName = re.sub('[\/:*?"<>|]','',originalName_title)+'.nfo'
# print(nfoFileName)
with open(javnum+"/"+nfoFileName, mode="w+", encoding="utf-8") as file:
    for i in nfoContent:
        file.write(i+"\n") 
# 重新命名影片名稱與nfo相同
os.rename(javnum+"/"+videoname, javnum+"/"+originalName_title+videotype)

# 2021.08.02 : 爬蟲資料對比迴圈
# 2021.08.03 : 圖片下載，nfo檔案編寫，與建立，資料夾複製，與隱藏(修改圖片大小、類型，刪減多餘文字)
# 2021.08.04 : 抓取資料夾內影片檔案名稱，移動與複製檔案，改善各種bug，不同影片號分析，並打包成EXE
#     (一早被外面施工與臭味勳到，睡不著，吃個早餐繼續寫)
# 2021.08.06 : 維修nfo錯誤斜線\的問題，標題長度
#     FileNotFoundError: [Errno 2] No such file or directory: '300NTK-273/300NTK-273_河北はるな - 美Gカップサンタは美パイパン！！彼氏にドタキャンされて地元の悪友とサンタコスパーティー！！押しに激弱の美白G乳のピンク乳首に生クリームトッピング！！敏感パイパンは手マンで大潮連発！！なし崩しで中出しSEX！！ /ラブホドキュメンタリー休憩2時間/34 (2019).nfo'
