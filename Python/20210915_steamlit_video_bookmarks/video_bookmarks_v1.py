# ---
# 讀取資料夾圖片
# 分析時間並抓取網址
# 存成csv檔案
# 從csv讀取->呈現成Table
# 可選擇標題與時間點
# TODO 時間也要變成t1,t2,t3,t4 (還要保留之後可擴充...)
# TODO 確認影片正確值
# ---

# 將圖片檔名轉成 圖片檔名、影片名稱、標記時間、創建日期
import pathlib
import os

# from pathlib import Path

import datetime

# from numpy.core.defchararray import index
from youtubesearchpython import VideosSearch
import streamlit as st
# from streamlit import components
import pandas as pd

import shutil

from streamlit_tags import st_tags, st_tags_sidebar
from ast import literal_eval

# CSS
st.markdown(
    """
    <style>
    .img-time {
        width: 100%;
    }
    </style>
    <style>
    html, body { height: 100%; }
    body { overflow: hidden; margin: 0; }
    iframe {height: 100%; width: 100%;}
    .element-container{}
    </style>

    <style>
    .video-container {
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 56.25%;
    }
    .video-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    </style>
    
    """,
    unsafe_allow_html=True,
)
taglist = []

# 將資料夾圖片列表，資料化，並加入csv

# 搜尋資料夾folder內圖片，轉成[二維list]傳出
def scanFolder():
    folder = "scan/"
    folderPath = pathlib.Path(__file__).parents[0].joinpath(folder)
    folderPathNew = pathlib.Path(__file__).parents[0].joinpath("res/")
    folderIter = folderPath.iterdir()
    finalOutput = []

    # def itemInput(imgName):
    def setData(imgName):
        # 圖片檔名、影片名稱 # ! 像這種傳入檔案的不同命名很重要的，應該要多檔案提早測試
        # CLR: filePath要把從list存成pands時，出問題的原因? 來自 folderPath是物件WindowsPath('g:/my_coding/...') # ?? 那為什麼原本可以..
        adjustfilePath = str(folderPathNew.joinpath(imgName))  # 輸出後存放的，新的資料夾+檔案名稱
        videoNameList = imgName.split(" ")[0:-2]
        videoName = " ".join(videoNameList)

        # 標記時間
        _timeMark = imgName.split(" ")[-2]
        if len(_timeMark.split("-")) == 3:
            timeHH = _timeMark.split("-")[2].zfill(2)
        else:
            timeHH = "00"
        timeMM = _timeMark.split("-")[0].zfill(2)
        timeSS = _timeMark.split("-")[1].zfill(2)  # 時間補零

        # 創建日期
        _created_time = os.path.getmtime(filePath)
        _created_timeObj = datetime.datetime.fromtimestamp(_created_time)  # 轉時間物件
        created_date = _created_timeObj.strftime("%Y-%m-%d")  # 2021-09-12
        # created_time = _created_timeObj.strftime("%H%M%S")  # 214303

        return videoName, timeHH, timeMM, timeSS, created_date, adjustfilePath

    def searchYT(videoName):
        # 上網並搜索 影片名稱網址、影片頻道名稱、合併 網址與標記時間
        videosSearch = VideosSearch(videoName, limit=1)
        urlink = dict(videosSearch.result()["result"][0])["link"]
        return urlink

        # 移動圖片

    def moveimg(filePath, adjustfilePath):
        source = pathlib.Path(filePath)
        destination = pathlib.Path(adjustfilePath)
        shutil.move(source, destination)

    folerIterlist = list(enumerate(folderIter))
    for i, imgPath in folerIterlist:
        imgName = imgPath.parts[-1]
        filePath = str(folderPath.joinpath(imgName))  # 原有資料夾+檔案名稱
        itemOutput = []
        videoName, timeHH, timeMM, timeSS, created_date, adjustfilePath = setData(
            imgName
        )
        timeMark = timeHH + ":" + timeMM + ":" + timeSS
        # itemOutput.extend([videoName, timeMark, created_date])
        # 確認影片名稱跟上一輪是否相同，[i-1]最開始會變成-1
        if i == 0:
            prevVideoName = "None"
        else:
            prevVideoName = " ".join(folerIterlist[i - 1][1].parts[-1].split(" ")[0:-2])
        print(videoName)
        print(prevVideoName)
        # ?? 但原因不明 enumerate迴圈，裡面在塞enumerate應用，就會造成迴圈跑一次就停
        if videoName == prevVideoName:
            print("Same")
        else:
            print("Different")
            urlink = searchYT(videoName)
        urlinkWithTime = urlink + "#t=" + timeMM + "m" + timeSS + "s"

        # import random
        # tags = ", ".join(random.choice("a", "b", "c", "d", 2)) # 測試用
        tags = ""
        itemOutput = [
            videoName,
            timeMark,
            created_date,
            urlinkWithTime,  # 之後轉alink
            urlinkWithTime,
            adjustfilePath,
            tags,
        ]
        finalOutput.append(itemOutput)
        moveimg(filePath, adjustfilePath)
        print("one file done")

    # 將list轉成panda形式
    pandaDF = pd.DataFrame(
        finalOutput,
        columns=["Name", "TimeMark", "SnapTime", "alink", "link", "FilePath", "Tags"],
    )
    # 將alink一欄，轉成可點擊href<a>標籤形式
    pandaDF["alink"] = pandaDF["alink"].apply(make_clickable)
    return pandaDF


# Youtube 圖片、標籤時間點播放
def st_imglink(url, link=""):
    import base64

    # 檢查檔案是否存在
    if os.path.isfile(url):
        showimg = st.markdown(
            f"""
            <div class="img-container">
                <a target="_blank" class="img-link" href="{link}">
                    <img class="img-time" src="data:image/png;base64,{base64.b64encode(open(url, "rb").read()).decode()}">
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return showimg
    else:
        print("檔案不存在。")

    # except ValueError as err:
    #     print("No Picture")


# 將行資料apply成link
def make_clickable(link):
    return f'<a target="_blank" href="{link}">Link</a>'


# ---< 存成excel檔案後重新讀取 >---

# 新建讀取資料夾的pdf，讀excel轉pd，在原excel之後面
xlsxfileName = "./20210915_steamlit_video_bookmarks/modified.xlsx"

if st.button("First Scan and save"):
    newdf = scanFolder()
    newdf
    newdf.to_excel(xlsxfileName, index=False)  # 前面乾淨
    st.success("Here you go!")

# 本來功能: 同時合併與創建
if st.button("Scan, merge and save"):
    newdf = scanFolder()
    originaldf = pd.read_excel(xlsxfileName)  # !沒有檔案的話，也沒辦法讀取，會出問題的
    mergedf = originaldf.append(newdf)
    # TODO 合併表格，需要在sort名稱跟TimeMark
    mergedf
    # if st.button("Save"):
    mergedf.to_excel(xlsxfileName, index=False)
    st.success("Here you go!")

if st.checkbox("讀取excel資料庫"):
    # # 讀取，記得用read_excel
    df = pd.read_excel(xlsxfileName)  # , index=False)  # encoding="utf-8"

# ---< 建立streamlit >---
#! with sidebar的內容會自動讀，也就是說如果初始檔案沒有的話，就會報錯
if st.checkbox("顯示側邊攔"):
    with st.sidebar:
        nameChoices = tuple(df["Name"].drop_duplicates())  # 將name整理成唯一命名
        searchName = st.selectbox("Select a name", nameChoices)
        # 篩選名稱
        nameCondition = df["Name"] == searchName
        selectedList = df.loc[nameCondition]  # .reset_index()重設index會多出一行

        # 設立時間選擇上限
        searchTimeMark = st.number_input(
            "give a number",
            min_value=0,
            max_value=selectedList["TimeMark"].shape[0] - 1,
            step=1,
        )

        # 隱藏 Name(0) FilePath(4) 與 snap(2) 並轉成html table
        # TODO: 這邊顯示的index不是0123
        showTable = selectedList.iloc[:, [1, 3]].to_html(escape=False)
        st.write(showTable, unsafe_allow_html=True)

        keywords = st_tags_sidebar(
            label="# Enter Keywords:",
            text="Press enter to add more",
            value=["a","b"],
            suggestions=taglist,
            maxtags=10,
            key="searchTags",
        )

        tagsCondition = df["Tags"].map(lambda tags: all(tag in tags for tag in keywords))
        
        # searchitemMark = st.sidebar.number_input(
        #     "give a number",
        #     min_value=0,
        #     max_value=df["Tags"].shape[0] - 1,
        #     step=1,
        # )

        timeSelected = True #(df["TimeMark"] == "10:02")
        condition = tagsCondition & timeSelected
        st.write(df[condition])

        if df[condition].shape[0]==1:
        # if st.sidebar.checkbox("Click to change tags"):
            save_keywords = st_tags_sidebar(
                label="# Enter Keywords:",
                text="Press enter to add more",
                value=keywords, # df.loc[condition,'Tags']
                suggestions=taglist,
                maxtags=10,
                key="savingTags",
            )
            st.write(df.loc[condition,'link'])
            if st.button("Save tags"):
                df.loc[condition,'Tags'] = ", ".join(save_keywords)
                df.loc[condition,'Tags']
                df.to_excel(xlsxfileName, index=False)
                st.success("Here you go! Data is been saved!")
            else:
                st.write(df.loc[condition,'Tags'])

        # 方法一 list，map、literal_eval  
        # tagCondition = keywords[0]
        # rows = df[df["Tags"].map(lambda tags: tagCondition in tags)]
        # searchitemMark = st.sidebar.number_input(
        #     "give a number",
        #     min_value=0,
        #     max_value=rows["Tags"].shape[0] - 1,
        #     step=1,
        # )

        # st.write(rows)
        # row = rows.iloc[searchitemMark, :]
        # st.write(row)
        # test = literal_eval(row["Tags"])
        # st.write(test)
        # test.append("f")
        # row["Tags"] = str(test)
        # st.write(row)

# 顯示iframe，並且能夠調整開始時間，以及自適應寬度。直接用st.video則無法調整開始時間
# @link [【Day 28】Youtube iframe 影片自動縮放大小 - CSS 解決方法 - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10252882) at 2021/9/19
# @link [像图片一样缩放iFrame CSS宽度100％ - ITranslater](https://www.itranslater.com/qa/details/2582500352734004224) at 2021/9/19 考慮
# ! iframe網址記得修改
# 1.內嵌playlist:
# https://www.youtube.com/embed?listType=playlist&list=PLJV_el3uVTsOK_ZK5L0Iv_EQoL1JefRL4
# 2.內嵌一部影片
# https://www.youtube.com/embed/XnyM3-xtxHs
# st.video("https://www.youtube.com/watch?v=z6dNAdtWdJk#t=6m37s")
# st.video("https://www.youtube.com/embed/klZNNUz4wPQ?start=397&end=424&rel=0")
# ---[ pandas: .values - df轉回列表list值 ]---
if df[condition].shape[0]==1:
    emlink = df.loc[condition, 'link'].values[0].replace('watch?v=','embed/')
    st.markdown(
        f"""
        <div class="video-container">
            <iframe width="100%" height="523.5px" id="ytplayer" type="text/html" src="{emlink}" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="0">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

# component.iframe("""
#     https://www.youtube.com/embed/zaoiriEbncc""" , scrolling = True , height = 350)

# 顯示選取圖片
# ! FileNotFoundError: [Errno 2] No such file or directory: 'g:\\my_coding\\Python\\20210915_steamlit_video_bookmarks\\res\\Using Pathlib in Python 14-35 screenshot.png' 指的是檔案根本沒在裡面!!! 不是路徑有問題!!
if st.checkbox("顯示圖片連結"):
    st.title(selectedList["Name"].iloc[int(searchTimeMark)])
    st.subheader(selectedList["TimeMark"].iloc[int(searchTimeMark)])
    # st.write("----",selectedList["TimeMark"].iloc[int(searchTimeMark)],"----")
    url = pathlib.Path(selectedList["FilePath"].iloc[int(searchTimeMark)])
    st_imglink(url, selectedList["link"].iloc[int(searchTimeMark)])


# 將資料整理成panda
# from pretty_html_table import build_table

# body = """
# <html>
# <head>
# </head>

# <body>
#         {0}
# </body>

# </html>
# """.format(build_table(df, 'blue_light'))
# df

# 將資料匯出成csv

# 資料按照group讀出，建立可搜索標籤
# %%
# 雙xlsx合併

# import pandas as pd
# import pathlib
# path1 = pathlib.Path(r"G:\my_coding\Python\20210915_steamlit_video_bookmarks\folder1.xlsx")
# path2 = pathlib.Path(r"G:\my_coding\Python\20210915_steamlit_video_bookmarks\folder2.xlsx")
# originaldf = pd.read_excel(path1)
# newdf = pd.read_excel(path2)
# mergedf = originaldf.append(newdf)
# mergedf


# %%
# tuple轉list用.extend方式將每個元素加到列表內，
# def abc():
#     a = 1
#     b = 2
#     c = 3
#     return a, b, c
# lili = [0]
# e, f, g = abc()
# lili.extend([e, f, g])
# print(lili)
# print(a[0],b,c) #?? 這樣用會不會有問題呢?

# %%
# 篩選關鍵字標籤tags，的列
import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["aaa", "bbb", "ccc"],
        "tags": [["a", "b", "c"], ["b"], ["c"]],
        "b": [3, 2, 3],
        "c": [6, 5, 4],
    }
)
# ?? 為什麼這些tags輸出時不會有'a'的符號。[a, c, f]

# ---[pandas: 找出單項在文字裡，多項在文字的列 ]---
df[df["tags"].map(lambda tags: "b" in tags)]  # 對行，做map的處理，回傳行bool
row = df[df["tags"].map(lambda tags: "b" in tags and "c" in tags)]
row
# ?? 為什麼這樣抓不到tags呢
# tagCondition = df['tags'] == '[c]'
# selectedList = df.loc[tagCondition]
# selectedList

# row
# type(row)  # *pandas.core.frame.DataFrame
# type(row["tags"])  # *pandas.core.series.Series
# row["tags"]
# row["tags"][0].append("f")  # CLR [0] = index
# row["tags"][0].remove("b")
# df

# 為'aaa'那一列，加入關鍵字
# ---[pandas: 找出單項相等，多重相等的列 ]---
# df[df['Name']=="aaa"]
# df[df['Name'].isin(['aaa','bbb']) & df.b.isin([3])] # 對行，做isin的處理，回傳行bool # ??&可以 and卻不行
# 多重排序
# df.sort_values(by=['b','c'], ascending=[True,False])

# %%
# ---[ pandas: 修改[list]資料的方式 ]---
# !存成excel在讀出來，出來，list就不能用了
# 看起來numpy就是不能用多維度
# @link [python - Pandas DataFrame stored list as string: How to convert back to list - Stack Overflow](https://stackoverflow.com/questions/23111990/pandas-dataframe-stored-list-as-string-how-to-convert-back-to-list/23112008) at 2021/9/18
# CLR 原來利用literal_eval可以辨別str的資料耶
""" 
import pandas as pd
from ast import literal_eval

xlsxfileName = "modified.xlsx"
# 失敗 df = pd.read_excel(xlsxfileName, dtype={'Tags':list})
# 失敗 df = pd.read_csv(xlsxfileName, converters={'Tags': eval})
df = pd.read_excel(xlsxfileName)
# selected = df[df['Tags'].map(lambda tags: 'e' in tags) & (df['TimeMark']=='02:44')]
selected = df[df["Tags"].map(lambda tags: "a" in tags) & (df["TimeMark"] == "10:02")]

# 存不回去 : A value is trying to be set on a copy of a slice from a DataFrame
test = literal_eval(selected["Tags"][6])
test.append("f")
test.remove("a")
df["Tags"][6] = str(test)
df
 """
# @link [pandas的SettingWithCopyWarning警告出现的原因和如何避免_haolexiao的专栏-CSDN博客](https://blog.csdn.net/haolexiao/article/details/81180571) at 2021/9/18
# 如果使用這種方式，會無法存入資料
# selected.loc[6,['Tags']] = str(test)

# 第一次問題
# type(selected) # *pandas.core.frame.DataFrame
# type(selected['Tags']) # *pandas.core.series.Series
# # selected['Tags'][6] #??怎麼就是不能轉list

# 其他方式
# row = selected.iloc[1] # integer-location
# type(row) # *pandas.core.series.Series 同樣是series但卻不一樣
# type(row['Tags'])
# row = df[df['Name'].isin(["好和弦教你做 8-bit 音樂！懷舊電玩風～"]) & df['TimeMark'].isin(['02:44'])]
# row
# %%
# ----withoulist 的方式----
""" 
import pandas as pd
from ast import literal_eval

xlsxfileName = "modified - wihtoulist.xlsx"
# 失敗 df = pd.read_excel(xlsxfileName, dtype={'Tags':list})
# 失敗 df = pd.read_csv(xlsxfileName, converters={'Tags': eval})
df = pd.read_excel(xlsxfileName)
# df['Tags'].isin(['b'])
# ! 要記得括號()
condition = df["Tags"].map(lambda tags: "a" in tags) & (df["TimeMark"] == "10:02")
# @link [Pandas SettingwithCopyWarning 警告處理](https://yentingli.blogspot.com/2019/09/pandas-settingwithcopywarning.html) at 2021/9/19
# selectedtag = df[condition].copy()
# selectedtag['Tags']
# ! 一句話就可以修改資料了，還用上面的!!! 三小
df.loc[condition,'Tags'] = df.loc[condition,'Tags'] +', e'
df 
"""
# selectedtag

# selectedtag.iloc[:, 6] = str(value)
# df
# selectedtag['Tags'] = literal_eval(selectedtag['Tags']) +', e'
# df

# 存不回去 : A value is trying to be set on a copy of a slice from a DataFrame
# test = literal_eval(selected["Tags"][6])
# test.append("f")
# test.remove("a")
# df["Tags"][6] = str(test)
# df

# %%
# imgName = "6-28"
# try :
#     imgName.split("-")[2]
# except IndexError:
#     print("Game Over")

# if len(imgName.split("-")) == 3:
#     print("Game Over")
# else:
#     print(imgName.split("-")[1])

import time

str_time = "2020-12-12 12:12:12"

# 字串轉時間
t = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
print(t)

# 時間轉字串
str_time_2 = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(str_time_2)

timeMark = "00:03:15"
strToTime = time.strptime(timeMark, "%H:%M:%S")
totalsecs = strToTime.tm_min * 60 + strToTime.tm_sec
totalsecs
# %%
lili = [1, 2]
litwo = [3, 4]
lili.extend(litwo)
lili
# %%
# ---[ any(),all(): 判斷是否list多字串是否在另外的字串裡面 ]---
a = "I Love Crystal!And I Hate Tom!"
any_list = ["Jessie", "Tom", "Crystal"]
print(any(name in a for name in any_list))
every_list = ["Hate", "Tom", "Love"]
print(all(name in a for name in every_list))

# matches = [x in a for x in every_list]
# matches = [x for x in every_list if x in a]
# %%
