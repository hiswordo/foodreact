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

import time

# Steamlit CSS
# CSS
# 圖片連結: img-time、影片iframe: vidoeo-container
st.markdown(
    """
    <style>
    .img-time {
        width: 100%;
    }
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

# 初始資料 - 建立資料夾路徑、標籤
inFolder = "scan/"
outFolder = "res/"
inFolderPath = pathlib.Path(__file__).parents[0].joinpath(inFolder)
outFolderPath = pathlib.Path(__file__).parents[0].joinpath(outFolder)
taglist = []


def setData(imgName):
    # TODO : 這裡僅以youtube截圖形式判別
    # 影片名稱: 圖片名以" "空格區分出name + time + 副檔名
    videoName = " ".join(imgName.split(" ")[0:-2])

    # 標記時間
    _timeMark = imgName.split(" ")[-2]
    if len(_timeMark.split("-")) == 3:
        timeHH = _timeMark.split("-")[2].zfill(2)
    else:
        timeHH = "00"
    timeMM = _timeMark.split("-")[0].zfill(2)
    timeSS = _timeMark.split("-")[1].zfill(2)  # 時間補零

    # 創建日期
    _created_time = os.path.getmtime(inFolderPath.joinpath(imgName))
    _created_timeObj = datetime.datetime.fromtimestamp(_created_time)  # 轉時間物件
    created_date = _created_timeObj.strftime("%Y-%m-%d")  # 2021-09-12
    # created_time = _created_timeObj.strftime("%H%M%S")  # 214303

    # 轉移後的資料夾路徑+圖檔名
    adjustfilePath = str(outFolderPath.joinpath(imgName))

    return videoName, timeHH, timeMM, timeSS, created_date, adjustfilePath


def searchYT(videoName):
    # 上網並搜索 影片名稱網址、影片頻道名稱、合併 網址與標記時間
    videosSearch = VideosSearch(videoName, limit=1)
    urlink = dict(videosSearch.result()["result"][0])["link"]
    return urlink


def moveimg(filePath, adjustfilePath):
    source = pathlib.Path(filePath)
    destination = pathlib.Path(adjustfilePath)
    shutil.move(source, destination)


# TODO: 如果傳入Link標題用時間，會更好看一點
def make_clickable(link):
    return f'<a target="_blank" href="{link}">Link</a>'


# Youtube 圖片、標籤時間點播放
def st_imglink(url, link=""):
    import base64

    # 檢查檔案是否存在
    if os.path.isfile(url):
        # ?? 為什麼自動多了"在兩側呢?
        showimg = st.markdown(
            f"""
            <div class="img-container">
                <a target="_blank" class="img-link" href={link}> 
                    <img class="img-time" src="data:image/png;base64,{base64.b64encode(open(url, "rb").read()).decode()}">
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return showimg
    else:
        print("檔案不存在。")


def getSeconds(str_time):
    strToTime = time.strptime(str_time, "%H:%M:%S")
    totalSecs = strToTime.tm_hour * 60 * 60 + strToTime.tm_min * 60 + strToTime.tm_sec
    return str(totalSecs)


# 圖片資料分析
# ---< 1 分析資料夾 >---
def scanFolder():
    # 初始資料 - img item資料清單
    folderIter = inFolderPath.iterdir()
    itemslist = []  # finalOutput

    # 1.1 路徑+圖片逐次讀入
    # 1.2 避免與上循環名字相同: ，使用enumerate轉成list同時傳入
    folerIterlist = list(enumerate(folderIter))
    for i, imgPath in folerIterlist:
        # 初始資料 - 圖片名、路徑合併、圖片item空list
        imgName = imgPath.parts[-1]
        filePath = str(inFolderPath.joinpath(imgName))  # 原有資料夾+檔案名稱
        itemOutput = []

        # 1.3 # 將圖片檔名解包成 : 影片名稱、標記時間*3、紀錄日期、圖片路徑(新)、
        # TODO 圖片路徑是絕對路徑，需要修改
        videoName, timeHH, timeMM, timeSS, created_date, adjustfilePath = setData(
            imgName
        )

        # 1.3 合併成完整標記時間
        timeMark = timeHH + ":" + timeMM + ":" + timeSS

        # 1.4 確認影片名稱跟上一輪是否相同，[i-1]最開始會變成-1
        if i == 0:
            prevVideoName = "None"  # 第一次沒有比較的，直接命前一次為None
        else:
            prevVideoName = " ".join(folerIterlist[i - 1][1].parts[-1].split(" ")[0:-2])
        if videoName == prevVideoName:
            pass  # the same，跳過搜尋YT連結部分
        else:
            urlink = searchYT(videoName)

        # 1.3 合併成youtube link with 時間標記
        urlinkWithTime = urlink + "#t=" + timeMM + "m" + timeSS + "s"

        import random

        tags = ", ".join(random.choices(["a", "b", "c", "d"], k=2))  # 測試用
        # tags = ""
        description = ""
        linkchecked = False  # 影片連結確認正確

        # 1.5 存入img item list中，並合併到itemslist上
        itemOutput = [
            videoName,
            timeMark,
            created_date,
            urlinkWithTime,  # 之後轉alink
            urlink,  # 存沒有加過時間的link # 乾淨link
            adjustfilePath,
            tags,
            description,
            linkchecked,
        ]
        itemslist.append(itemOutput)

        # 1.6 移動img到res新資料夾
        moveimg(filePath, adjustfilePath)
        print("one file done")

    # 將list轉成panda形式
    pandaDF = pd.DataFrame(
        itemslist,
        columns=[
            "Name",
            "TimeMark",
            "SnapTime",
            "aLink",
            "Link",
            "FilePath",
            "Tags",
            "Descri",
            "LinkCK",
        ],
    )

    # 將alink一欄，轉成可點擊href<a>標籤形式
    # 將行資料apply成link
    pandaDF["aLink"] = pandaDF["aLink"].apply(make_clickable)
    return pandaDF


# ---< 2 存成excel檔案後重新讀取 >---
# 新建讀取資料夾的pdf，讀excel轉pd，在原excel之後面
xlsxfileName = "./20210915_steamlit_video_bookmarks/modified.xlsx"

if st.sidebar.button("First Scan and save"):
    newdf = scanFolder()
    newdf
    newdf.to_excel(xlsxfileName, index=False)  # 前面乾淨
    st.success("Here you go!")

# 本來功能: 同時合併與創建
if st.sidebar.button("Scan, merge and save"):
    newdf = scanFolder()
    originaldf = pd.read_excel(xlsxfileName)  # !沒有檔案的話，也沒辦法讀取，會出問題的
    mergedf = originaldf.append(newdf)
    # TODO 合併表格，需要在sort名稱跟TimeMark
    mergedf
    # if st.button("Save"):
    mergedf.to_excel(xlsxfileName, index=False)
    st.success("Here you go!")

if st.sidebar.checkbox("讀取excel資料庫", True):
    # # 讀取，記得用read_excel
    df = pd.read_excel(xlsxfileName)  # , index=False)  # encoding="utf-8"

# ---< 3 建立streamlit >---
#! with sidebar的內容會自動讀，也就是說如果初始檔案沒有的話，就會報錯
if st.checkbox("顯示側邊攔", True):
    with st.sidebar:
        # nameChoices = tuple(df["Name"].drop_duplicates())  # 將name整理成唯一命名
        # searchName = st.selectbox("Select a name", nameChoices)
        # # 篩選名稱
        # nameCondition = df["Name"] == searchName
        # selectedList = df.loc[nameCondition]  # .reset_index()重設index會多出一行

        # # 設立時間選擇上限
        # searchTimeMark = st.number_input(
        #     "give a number",
        #     min_value=0,
        #     max_value=selectedList["TimeMark"].shape[0] - 1,
        #     step=1,
        # )

        # # 隱藏 Name(0) FilePath(4) 與 snap(2) 並轉成html table
        # # TODO: 這邊顯示的index不是0123
        # showTable = selectedList.iloc[:, [1, 3]].to_html(escape=False)
        # st.write(showTable, unsafe_allow_html=True)

        keywords = st_tags_sidebar(
            label="# Tags搜索:",
            text="Press enter to add more",
            value=["a", "b"],
            suggestions=taglist,
            maxtags=10,
            key="searchTags",
        )

        tagsCondition = df["Tags"].map(
            lambda tags: all(tag in tags for tag in keywords)
        )

        # searchitemMark = st.sidebar.number_input(
        #     "give a number",
        #     min_value=0,
        #     max_value=df["Tags"].shape[0] - 1,
        #     step=1,
        # )

        timeSelected = True  # (df["TimeMark"] == "10:02")
        condition = tagsCondition & timeSelected

        # if df[condition].shape[0]==1:
        # if st.sidebar.checkbox("Click to change tags"):
        if st.checkbox("集體修改Tags標籤"):
            save_keywords = st_tags_sidebar(
                label="# Tags標籤:",
                text="Press enter to add more",
                value=keywords,  # df.loc[condition,'Tags']
                suggestions=taglist,
                maxtags=10,
                key="savingTags",
            )
            # st.write(df.loc[condition, "Link"])
            if st.button("Save tags"):
                df.loc[condition, "Tags"] = ", ".join(save_keywords)
                df.loc[condition, "Tags"]
                df.to_excel(xlsxfileName, index=False)
                st.success("Here you go! Data is been saved!")
            else:
                st.write(df.loc[condition, "Tags"])

        st.subheader("Tags搜索結果")
        # ! drop=True會幫忙刪掉原本index
        st.write(df[condition].iloc[:, [0, 2]].reset_index(drop=True))

# TODO: 圖片連結CSS，4x8排列?
# 標籤搜索後，顯示圖片連結
# if st.checkbox("顯示圖片連結"):
#     for i in range(df.loc[condition].shape[0]):
#         st.subheader(df.loc[condition, "TimeMark"].values[i])
#         # 圖片路徑
#         imgurl = pathlib.Path(df.loc[condition, "FilePath"].values[i])
#         # 將 aLink 去掉tag轉成裡面的url網址
#         imgurlWithTime = (
#             df.loc[condition, "aLink"]
#             .values[i]
#             .replace('<a target="_blank" href=', "")
#             .replace(">Link</a>", "")
#         )
#         st_imglink(imgurl, imgurlWithTime)

# TODO 新功能，顯示一張照片連結就好
# @st.cache
def showimg(j):
    imgShowlink = []
    imgTimelink = []
    for i in range(df.loc[condition].shape[0]):
        # 圖片路徑
        imgurl = pathlib.Path(df.loc[condition, "FilePath"].values[i])
        # 將 aLink 去掉tag轉成裡面的url網址
        imgurlWithTime = (
            df.loc[condition, "aLink"]
            .values[i]
            .replace('<a target="_blank" href=', "")
            .replace(">Link</a>", "")
        )
        imgShowlink.append(imgurl)
        imgTimelink.append(imgurlWithTime)

    return st_imglink(imgShowlink[j], imgTimelink[j])


if st.sidebar.checkbox("顯示圖片連結", key="second"):
    if df.loc[condition].shape[0] == 1:
        j = 0
    else:
        j = st.slider("number", min_value=0, max_value=(df.loc[condition].shape[0] - 1))
    st.subheader(df.loc[condition, "TimeMark"].values[j])
    showimg(j)


# 顯示iframe，並且能夠調整開始時間，以及自適應寬度。直接用st.video則無法調整開始時間
# ! iframe網址記得修改embed
# TODO: 有廣告!
if df[condition].shape[0] == 1:
    emlink = df.loc[condition, "Link"].values[0].replace("watch?v=", "embed/")
    secs = getSeconds(df.loc[condition, "TimeMark"].values[0])
    finalEmlink = emlink + "?start=" + secs + "&rel=0"
    st.subheader(df.loc[condition, "TimeMark"].values[0])
    st.markdown(
        f"""
        <div class="video-container">
            <iframe width="100%" height="523.5px" id="ytplayer" type="text/html" src="{finalEmlink}" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="0">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )
