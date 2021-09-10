
# TODO #Python List
"""
VsCode Extension List
* GitLens : 將兩個 branch 分支進行整體的代碼對比
"""


# import的list
# import shutil # buffer資料的處理
# import os # 資料夾相關處理
# pip install pypiwin32
# pip install eel
# pip install tk # tkinter

# 讓pythin轉exe
# pip install pyinstaller 

# import urllib.parse
# 官方文件:https://docs.python.org/zh-tw/3/library/urllib.parse.html

# bs4
# soup["src"]等同soup.attrs.get("src")
# 一旦find()執行，沒找到就得停止在那一行程是嗎??

# pip install matplotlib #好像不需要耶，要幹嘛

# Python程式習慣、學到的東西
    # 001.變數命名: 首字小寫
    # 002.index()的結果在前面
    # 003.[bs4]抓取屬性值時小心原本就是None值，["style"]抓取標籤屬性的時候，連續動作都不行，find.find....
    # 004.[0:2]=[0]、[1]，[0:]=開始到最後，[1:-1]=第二個到倒數第一個
    # 005.for i in x，x是字串或list，數字的話要用range
    # 006.index()如果找不到會出現錯誤ValueError: substring not found，find()只會變-1值
    # 007.多行註解，連三'''這樣'''or"""000""""
    # 008.要注意版本資訊，有的代碼版本不一樣，可以用來做跳板查詢
    # 009.抓資料的同時，常常要想到如果沒抓到會怎麼了?
    # 010.str()可以自動移除前後空白

# wordtest = [1,2,3,4,5]
# print(wordtest[1:-1])   

# 觀念建置
    # 001.URL允許一部分ASCII字元（數位字母和部分符號），其他的字元（如漢字）是不符合URL標準的。需要進行URL編碼。
    # 002.def內的區域變數，是不會影響全域

# 前置作業相關
# 001.pip install安裝完，有的需要重開程式

# vscode操作相關問題
# ‎001.焦點模式:ctrl+M‎ (會令tab無法空格，右下角blue bar:Tab Moves Focus)

# pip install Selenium 

# pip install wget
# Error: urllib.error.HTTPError: HTTP Error 403: Forbidden
    # Solution: 
"""
pip install cv2 #opencv
    切割圖片用
ERROR: Could not find a version that satisfies the requirement cv2 (from versions: none)
ERROR: No matching distribution found for cv2
    解決方法: pip install opencv-python
手冊:http://www.1zlab.com/wiki/python-opencv-tutorial/opencv-image-cut-select-roi/

pip install bs4 # beautiful soup
自訂屬性的抓法: idPage.find('a',attrs={'data-fancybox':'gallery'})
    <a data-fancybox="gallery" href="XXX"><img class="video-cover" src="XXX"/></a>
測試 https://www.youtube.com/watch?v=iUIqPXn4zKs
    imgLink = soup.attrs.get("src") #所有圖片網址
    imgContent = requests.get(imgLink).content
"""


# ! 錯誤錦囊
# 0 positional arguments but 1 was given
    # def acb(?) 沒有參數可以輸入

# TypeError: 'NoneType' object is not subscriptable
# AttributeError: 'NoneType' object has no attribute 'text'
    # 對一個None的東西做動作找屬性的動作，例如None["style"]，None.text
# IndentationError: unexpected indent
    # 有錯誤的縮排
# TypeError: object of type 'int' has no len()
    # 可能變數打錯，造成()裡面沒有值可以跑
# AttributeError: 'list' object attribute 'append' is read-only
    # list.append = 5 要改成 list.append(5)

# ! 錯誤錦囊saved
# SyntaxError: unexpected EOF while parsing
    # (少打另一邊的括號


# requests & shutil:爬取圖片
# 教學:https://www.youtube.com/watch?v=9unqUH0PYCI
# import requests
# import shutil # buffer資料的處理
# imgLink = "https://www.maxpixel.net/static/photo/1x/Aptitude-Test-Road-Sign-Testing-Test-Right-Of-Way-361514.png"
# filename = imgLink.split('/')[-1]
# res1 = requests.get(imgLink, stream=True) # 串流方式讀取的意思是??
# pic = open(filename,'wb') # 用filename的名稱開啟檔案，'wb'模式是??
# shutil.copyfileobj(res1.raw,pic) # 從res1把圖片複製到pic裡
# pic.close() # 關閉，會自動存檔?
# del res1 # 刪除暫存檔?

# # cv2:切割圖片
# # 教學:https://blog.gtwang.org/programming/how-to-crop-an-image-in-opencv-using-python/
# import cv2
# # 開啟並切割圖片
# img = cv2.imread("fanart.jpg")
# crop_img = img[0:579, 421:800]
# # 顯示圖片
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)
# # 寫入圖檔
# cv2.imwrite('crop.jpg', crop_img)

# # # cv2 & matplotlib:放大圖片(縮小)
# # # 教學:https://shengyu7697.github.io/python-opencv-resize/
# import cv2
# # from matplotlib import pyplot as plt  #好像不需要耶，要幹嘛?uninstall也可阿
# img = cv2.imread('BvRbA.jpg')
# imgEnlarge = cv2.resize(img, (380, 540), interpolation=cv2.INTER_CUBIC) #(x,y)
# cv2.imshow('Result', imgEnlarge)
# cv2.waitKey(0)
# cv2.imwrite('BvRbA_small.jpg', imgEnlarge)

# 維持縮放比例def
# import cv2
# def image_resize(image, width = None, height = None, inter = cv2.INTER_CUBIC):
#     # initialize the dimensions of the image to be resized and
#     # grab the image size
#     dim = None
#     (h, w) = image.shape[:2]

#     # if both the width and height are None, then return the
#     # original image
#     if width is None and height is None:
#         return image

#     # check to see if the width is None
#     if width is None:
#         # calculate the ratio of the height and construct the
#         # dimensions
#         r = height / float(h)
#         dim = (int(w * r), height)

#     # otherwise, the height is None
#     else:
#         # calculate the ratio of the width and construct the
#         # dimensions
#         r = width / float(w)
#         dim = (width, int(h * r))

#     # resize the image
#     resized = cv2.resize(image, dim, interpolation = inter)

#     # return the resized image
#     return resized

# 放大圖片(縮小) 利用已經有的模組比較看看??
# import os
# # PIL : Python Imaging Library
# from PIL import Image
# # os.mkdir('icon')
# size = (256,256)
# im = Image.open("poster.jpg").resize(size)
# im.save("foldertest3.ico")
# im.close()

# 測試失敗，圖片一定要正方形，不然會變形，損壞等
# 轉ico:https://segmentfault.com/a/1190000039042026

# 圖片縮放大小不失比例
# https://www.coder.work/article/91112
# 完整許多: https://www.codenong.com/44650888/

# list逐行存入檔案
# content=[]
# content.append("  <sorttitle></sorttitle>")
# content.append('  <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n<movie>')
# content.append("  "+"<set>ツンフワ小悪魔</set>")
# content.append("  "+"<year>2019</year>")
# content.append("  "+"<<top250></top250>")
# content.append("  "+"<id>SW-642</id>")
# content.append("  "+"<title>中文存看看</title>")

# print(content)
# with open("456.txt", mode="w+", encoding="utf-8") as file:
#     for i in content:
#         file.write(i+"\n")  #小心不要寫成file.write(content[i]) #TypeError: list indices must be integers or slices, not str


# 讀取頁面
# import urllib
# urllib.quote("中文") 轉正確網址列，python3後已經沒有了，要換成urllib.parse.quote("châteu", safe='')

import urllib.request as req
import urllib.parse
import bs4
import re
import os

#bs4分析頁面的function
def pageParser(url):
    request1=req.Request(url,headers={
        # "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
    })
    with req.urlopen(request1) as response1:
        data1=response1.read().decode("utf-8")
    root1=bs4.BeautifulSoup(data1,"html.parser") 
    return root1

# os.system("G:/X2ico/x2ico.exe poster.jpg")
f = os.popen("x2ico.lnk ", "w")
d = f.write_through()
f.close()
# decode（’utf - 8’）解码   把其他编码转换成unicode编码
# encode(’gbk’) 编码  把unicode编码转换成其他编码

# javnum = "NA-001"
# pageLink="https://javdb.com/search?q="+ javnum +"&f=all"
# idSearchPage = pageParser(pageLink)
# fNextLink = idSearchPage.find("a",class_="box") #搜尋結果的第一個連結 = 真正要連結
# nextLink = "https://javdb.com/"+fNextLink["href"]
# idPage = pageParser(nextLink)
# fanartonlyPicCK = idPage.find('a',class_="cover-container")
# if fanartonlyPicCK != None:
#     fanartPicLink = idPage.find('a',class_="cover-container").find_next()["src"]
#     print(fanartPicLink)
# else:
#     fanartPicLink = idPage.find('a',attrs={'data-fancybox':'gallery'})["href"] #第一個即是fanart，所以不用find_all
#     print("original"+fanartPicLink)

# title = page.find_all("div",class_="panel-block")[8].find_next().find_next().text
# if title.find("♀")==None:
#     print("nothing")
# else:
#     print("well") 

# 日文的decode (Shift-JIS/EUC-JP)
# decodeword = urllib.parse.unquote("%b5%c8%cc%ee%ce%a4%c6%e0","EUC-JP")
# print(decodeword)

# 循環檢查號碼
# 素人女優 [LUXU][SIRO][GANA][MAAN][NTK][JAC][EVA][SCUTE]
# comparNums = ["LUXU", "SIRO", "GANA", "MAAN", "NTK", "EVA"] #"JAC","SCUTE"不用
# javnum = "GANA-2531"
# for comparNum in comparNums:
#     checkJavN = javnum.upper().find(comparNum)
#     if checkJavN != -1: # or content.find("♀")==None:
#         # av-wiki用番號搜尋，取得女優name
#         avwikiPageLink = "https://av-wiki.net/?s="+javnum+"&post_type=product"
#         avwikiSearchPage = pageParser(avwikiPageLink)
#         avwikiAvStarName = avwikiSearchPage.find("p",class_="actress-name").find_next().text
#         if avwikiAvStarName != "(≥o≤)":
#             avwikiAvStarLink = avwikiSearchPage.find("p",class_="actress-name").find_next().find_next()["href"] #備用
#             # javdb用name搜尋，取得女優pic
#             jpwdEncode = urllib.parse.quote(avwikiAvStarName,safe='中村')
#             javdbAvStarPageLink = "https://javdb.com/search?f=actor&q="+jpwdEncode
#             javdbAvStarPage = pageParser(javdbAvStarPageLink)
#             javdbAvStardiv = javdbAvStarPage.find("span",class_="avatar")["style"] #已經取出成純文字，python就會認定成str 
#             javdbAvStarPicLink = re.findall("\((.+?)\)",javdbAvStardiv)[0]  #篩選()的網址
#             print(javdbAvStarPicLink)
#         else:
#             print("sorrry,bro, can't find")


# 利用re正規表達式抓出()內的網址
# 教學:https://ithelp.ithome.com.tw/articles/10203352
# re之前的文字 background-image: url(https://jdbimgs.com/avatars/aa/aaGW.jpg) 
# import re
# url = re.findall("\((.+?)\)",javdbAvStar)[0]

# #刪除標題太長的部分，發現驚嘆號等標點符號，難以變動
# 176個
# tititle = "LUXU-1456 ラグジュTV 1438 生徒をセフレにする変態家庭教師が登場！「イケないこと」という背徳感に興奮し生徒を誘惑して手取り足取り性教育！それだけでは飽き足りず「撮られることに興奮したい」とラグジュTVに応募！自他共に認める美巨乳にガッツリくびれのスレンダーボディ！欲に飢えた淫乱美女を男優チ●ポでお仕置き！！"
# print(len(tititle))
# manytime = h2title.find(" ")
# nextword = h2title
# for i in range(manytime):
#     if len(nextword) > 150 : #保留50以內的文字，並斷在空白處
#         spacePos = nextword.rindex(" ")
#         nextword = h2title[0:spacePos]
#     else:
#         finaltitle = nextword
# print(finaltitle)

#【python內建模組- os/shutil】用python大量處理電腦上的檔案
# 教學:https://ithelp.ithome.com.tw/articles/10229950

# 獲取檔案檔名
# import os
# files = os.listdir() #['#cat', '123.txt']
# for inName in files:
#     tmp = os.path.splitext(inName)  #('#cat', '') ('123', '.txt')
#     if tmp[1] == '.mp4' or tmp[1] == '.ts':
#         javnum = tmp[0]
#         videoname = tmp[0]+tmp[1]
# print(javnum)
# print(videoname)

# # 获取目录下文件名
# files = os.listdir()
# # 图标大小
# size = (256,256)

# # 给图标文件单独创建一个icon目录
# if not os.path.exists('icon'):
#     os.mkdir('icon')
# for inName in files:

#     # 分离文件名与扩展名
#     tmp = os.path.splitext(inName)
#     # 因为python文件跟图片在同目录，所以需要判断一下
#     if tmp[1] == '.png':
#         outName = tmp[0] + '.ico'
#         # 打开图片并设置大小
#         im = Image.open(inName).resize(size)
#         try:
#             # 图标文件保存至icon目录
#             path = os.path.join('icon', outName)
#             im.save(path)
            
#             print('{} --> {}'.format(inName, outName))
#         except IOError:
#             print('connot convert :',inName)

#迴圈內的變數到外面還可以用
# words = [1,2,3,4,5]
# for i in words:
#     j = 30
#     j = i+1
#     print(j)
# print(j)



# 隱藏或顯示檔案
# 教學:https://blog.csdn.net/Mr_chenweida/article/details/108614857 https://www.cnblogs.com/dcb3688/p/4608016.html
# import os
# import shutil
# import win32con, win32api
# # numname = "NCC-5577"
# # shutil.copytree('G:\Coverbase01','BridgeName') 
# # os.rename("BridgeName", numname)
# # #shutil.copy(PathOf_SourceFileName.extension,TargetFolderPath)
# # # win32api.SetFileAttributes(numname+'/desktop.ini', win32con.FILE_ATTRIBUTE_HIDDEN) #win32con.FILE_ATTRIBUTE_HIDDEN=2 (數字喔不是字串喔)
# # win32api.SetFileAttributes(numname+'/desktop.ini', 2) #隱藏資料夾，寫法一樣

# # 檔案用外部程式開啟
# # 教學:https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/364537/
# # 文件:https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
# win32api.ShellExecute(0, 'open', 'G:/[Portable Mine]/EmEditor+17.5.0.x64/EmEditor.exe', '456.txt','',1) #如果不顯示要怎麼關掉?
# os.system('G:/EmEditor+17.5.0.x64/EmEditor.exe 456.txt') #但如果路徑上有[]，則會無法執行，有點麻煩??
# win32api.ShellExecute(0, "open", 'poster.jpg', '','',1) #這樣是可以用一般的開啟檔案jpg但仍不能用x2ico.exe
# os.system('G:/X2ico/x2ico.exe poster.jpg')
# win32api.ShellExecute(0, "drag", 'poster.jpg', 'G:/[Portable Mine]/X2ico/x2ico.exe','',1) 

# 移動檔案
# 教學:https://www.delftstack.com/zh-tw/howto/python/python-file-move/
# import shutil
# source = r'G:\my_python_project\123.txt' #檔案路徑前放置 r，使其成為原始字串，就不需要\轉/的麻煩
# destination = r'G:\my_python_project\NCC-5577\123.txt'
# shutil.move(source,destination)

# 創建資料夾封面資訊ini(但還是沒用，需重新設定)
# with open(javnum+"/desktop.ini", mode="w+") as file:
#     folderContent = "[.ShellClassInfo]\nIconResource=folder.ico,0"
#     file.write(folderContent) 


# python 找標點符號位置
# re
# try
# 推荐你看一本书:Code complete代碼大全2
# 第18章，讲的就是这种优化。
# Table-Driven Methods
# Python 用字典来优化if 多路判断。