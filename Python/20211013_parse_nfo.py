
# @link [【學習筆記】使用python批量讀取並修改xml檔案 - IT閱讀](https://www.itread01.com/content/1546434426.html) at 2021/10/14
# @link [xml.dom --- 文档对象模型 API — Python 3.10.0 說明文件](https://docs.python.org/zh-tw/3/library/xml.dom.html#xml.dom.Node.lastChild) at 2021/10/14
# @link 可能不錯用 [xml - Get the child elements of an XML element - Python code example - Kite](https://www.kite.com/python/examples/3471/xml-get-the-child-elements-of-an-xml-element) at 2021/10/14

#coding=utf-8
from xml.dom import minidom #等同 import xml.dom.minidom
import pandas as pd

###讀取單個xml檔案
dom=minidom.parse('./res/[MISM-082].nfo') # 開啟xml文件
root=dom.documentElement # 得到xml文件 dom
nodestag = root.childNodes # 將xml文件轉出child dom list
# print(nodestag)
# print(root) #<DOM Element: movie at 0x20d61f0>

# *列出所有node的tag跟value
# def nodeValueOut(input):
#     if input.firstChild.data 
#     input.firstChild.data

# !如果tag中間沒有夾資料值，會出現"AttributeError: 'NoneType' object has no attribute 'data'"
# 下一行跟中間沒有值的firstChild，因為沒有firstchild，print出來都是None
# ?? nodeValue = None & nodeType = 1 兩個都沒出現其他的值不知道為什麼
# !下一行的符號也會算一個dom... <DOM Text node "'\n  '">，所以childNodes出來的list，偶數都變成這個
# print(nodestag[4]) # <DOM Text node "'\n  '">
# print(nodestag[5]) # <DOM Element: sorttitle at 0x2d668d3> 
# print(nodestag[3].firstChild) # <DOM Element: originaltitle at 0x2d668ca> 的 child <DOM Text node "'おじさんの宝物にして'...">
# print(root.getElementsByTagName('fanart')[0].childNodes[1].firstChild.data) #?? 子標籤的子標籤真的要這麼麻煩嗎?

for x in nodestag:
    if x.nodeName == "fanart":
        print(x.nodeName,": ",root.getElementsByTagName('fanart')[0].childNodes[1].firstChild.data)
    elif x.nodeName == "actor":
        print(x.nodeName,"- Name: ",root.getElementsByTagName('actor')[0].childNodes[1].firstChild.data)
        print(x.nodeName,"- thumb: ",root.getElementsByTagName('actor')[0].childNodes[5].firstChild.data)
    else: 
        if x.nodeName != '#text':
            if x.firstChild is not None:
                print(x.nodeName,": ",x.firstChild.data)
            else:
                print(x.nodeName,": ","None")
# 轉到df裡面須修正
# df = pd.DataFrame({"document": (i.firstChild.nodeValue for i in nodestag)})
# print(df)
