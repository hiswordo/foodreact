import pathlib
import os

# from pathlib import Path

import datetime
from numpy.core.defchararray import upper

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
# TODO 設定在scanfolder裡面會更好一點，不然用重新整理才創建怪怪的
subfolders = os.listdir("./20210915_steamlit_video_bookmarks/scan")
for k in range(len(subfolders)):
    if not os.path.exists(outFolderPath.joinpath(subfolders[k])):
        os.mkdir(outFolderPath.joinpath(subfolders[k]))
taglist = []


def setData(imgName, subfolderName):
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
    _created_time = os.path.getmtime(inFolderPath.joinpath(subfolderName).joinpath(imgName))
    _created_timeObj = datetime.datetime.fromtimestamp(_created_time)  # 轉時間物件
    created_date = _created_timeObj.strftime("%Y-%m-%d")  # 2021-09-12
    # created_time = _created_timeObj.strftime("%H%M%S")  # 214303

    return videoName, timeHH, timeMM, timeSS, created_date


def searchYT(videoName):
    # 上網並搜索 影片名稱網址、影片頻道名稱、合併 網址與標記時間
    videosSearch = VideosSearch(videoName, limit=1)
    ytData = dict(videosSearch.result()["result"][0])
    ytlink = ytData["link"]
    ytDuration = ytData["duration"]
    ytId = ytData["id"]
    ytTitle = ytData["title"]
    ytChannel = ytData["channel"]["name"]
    print("Search Once")
    return ytlink, ytDuration, ytId, ytTitle, ytChannel


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
    itemslist = []  # finalOutput
    
    def onefolderScan(folerIterlist, subfolderName):
        for i, imgPath in folerIterlist:
            # 初始資料 - 圖片名、路徑合併、圖片item空list
            imgName = imgPath.parts[-1]
            # filePath = str(inFolderPath.joinpath(imgName))  # 原有資料夾+檔案名稱
            filePath = str(imgPath)  # 原有資料夾+檔案名稱
            itemOutput = []

            # 1.3 # 將圖片檔名解包成 : 影片名稱、標記時間*3、紀錄日期、圖片路徑(新)、
            # TODO 圖片路徑是絕對路徑，需要修改
            videoName, timeHH, timeMM, timeSS, created_date = setData(imgName, subfolderName)

                # 轉移後的資料夾路徑+圖檔名
            adjustfilePath = str(outFolderPath.joinpath(subfolderName).joinpath(imgName))
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
                ytlink, ytDuration, ytId, ytTitle, ytChannel = searchYT(videoName)
                # urlink = "https://www.youtube.com/watch?v="

            # 1.3 合併成youtube link with 時間標記
            ytlinkWithTime = ytlink + "#t=" + timeMM + "m" + timeSS + "s"

            # import random
            # tags = ", ".join(random.sample(["a", "b", "c", "d"], k=2))  # 測試用
            tags = subfolderName
            description = ""
            if ytTitle==videoName:
                linkchecked = True  # 影片連結確認正確
            else:
                linkchecked = False

            # 1.5 存入img item list中，並合併到itemslist上
            itemOutput = [
                videoName,
                timeMark,
                created_date,
                ytlinkWithTime,  # 之後轉alink
                ytlink,  # 存沒有加過時間的link # 乾淨link
                adjustfilePath,
                tags,
                description,
                linkchecked,
                ytDuration,
                ytId,
                ytChannel,
            ]
            itemslist.append(itemOutput)

            # 1.6 移動img到res新資料夾
            moveimg(filePath, adjustfilePath)
            print("one file done")

    # 初始資料 - img item資料清單
    # 1.1 路徑+圖片逐次讀入
    # 1.2 避免與上循環名字相同: ，使用enumerate轉成list同時傳入

    # folderIter = inFolderPath.iterdir()
    # folerIterlist = list(enumerate(folderIter))

    for i in range(len(subfolders)):
        # subfoldersPath = "./scan/" + subfolders[i]
        folderIter = inFolderPath.joinpath(subfolders[i]).iterdir()
        folerIterlist = list(enumerate(folderIter))
        onefolderScan(folerIterlist, subfolders[i])

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
            "Descri", # TODO 給輸入空格與搜尋欄位
            "LinkCK",
            "Duration",
            "ID", # TODO 修改網址配上ID會比較好吧?
            "Channel",
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

# 顯示excel所有資料，測試用
st.dataframe(df)

# TODO 改寫成儲存版? Tags推薦表，可以先給個基本屬性
# ---[ 不重複詞語list ]--- 
import nltk
preTaglist = ", ".join(list(df["Tags"]))
nltk_tokens = nltk.word_tokenize(preTaglist)
no_order = list(set(nltk_tokens))
no_order.remove(',')
taglist = no_order

# ---< 3 建立streamlit >---
#! with sidebar的內容會自動讀，也就是說如果初始檔案沒有的話，就會報錯
if st.checkbox("顯示側邊攔", True):
    with st.sidebar:
        keylabel = st.write("# Tags搜索:")
        keywords = st.multiselect(f"{keylabel}",taglist)  #?? 空行怎麼辦阿
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

        # TODO 目前先用搜索的，之後要用儲存的

        # !果然不需要這個額外modules耶...都有提示功能阿
        # keywords = st_tags_sidebar(
        #     label="# Tags搜索:",
        #     text="Press enter to add more",
        #     value=[],
        #     suggestions=taglist,
        #     maxtags=10,
        #     key="searchTags",
        # )

        # !多重tags包含在tags欄位內
        tagsCondition = df["Tags"].map(
            lambda tags: all(tag in tags for tag in keywords)
        )

        df[tagsCondition]

        # 標題選擇
        nameChoices = tuple(df[tagsCondition]["Name"].drop_duplicates())  # 將name整理成唯一命名
        searchName = st.selectbox("Select a name", nameChoices)
        # 篩選名稱
        nameCondition = df["Name"] == searchName

        # TODO 時間搜索似乎沒需要了
        # timeSelected = True  # (df["TimeMark"] == "10:02")
        condition = tagsCondition & nameCondition # & timeSelected

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
        st.write(df[condition].iloc[:, [0, 6, 9]].reset_index(drop=True))

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

def showVideo(j):
    # videoShowlink = []
    videoTimelink = []
    for i in range(df.loc[condition].shape[0]):
        # 圖片路徑
        emlink = df.loc[condition, "Link"].values[i].replace("watch?v=", "embed/")
        # 時間小時分鐘轉秒數總和secs
        secs = getSeconds(df.loc[condition, "TimeMark"].values[i])
        finalEmlink = emlink + "?start=" + secs + "&rel=0"
        # videoShowlink.append(emlink)
        videoTimelink.append(finalEmlink)
    
    mark1 = st.markdown(
        f"""
        <div class="video-container">
            <iframe width="100%" height="523.5px" id="ytplayer" type="text/html" src="{videoTimelink[j]}" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="0">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )

    return mark1

# TODO 新功能，顯示一張照片連結就好
# XXX @st.cache
# 顯示iframe，並且能夠調整開始時間，以及自適應寬度。直接用st.video則無法調整開始時間
# ! iframe網址記得修改embed
# TODO: 有廣告!
if st.sidebar.checkbox("顯示圖片連結&影片embeded", key="second"):
    if df.loc[condition].shape[0] == 1:
        j = 0
    else:
        j = st.slider("number", min_value=0, max_value=(df.loc[condition].shape[0] - 1))
    st.subheader(df.loc[condition, "TimeMark"].values[j])
    showimg(j)
    showVideo(j)

# if df[condition].shape[0] == 1:
    # st.subheader(df.loc[condition, "TimeMark"].values[j])
    # emlink = df.loc[condition, "Link"].values[0].replace("watch?v=", "embed/")
    # # 時間小時分鐘轉秒數總和secs
    # secs = getSeconds(df.loc[condition, "TimeMark"].values[0])
    # finalEmlink = emlink + "?start=" + secs + "&rel=0"
    # st.subheader(df.loc[condition, "TimeMark"].values[0])
    # st.markdown(
    #     f"""
    #     <div class="video-container">
    #         <iframe width="100%" height="523.5px" id="ytplayer" type="text/html" src="{finalEmlink}" frameborder="0"
    #         allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="0">
    #         </iframe>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )





# from datetime import time
# durationTime = st.slider(
#     "Schedule your appointment:",
#     value=time(3,5),
#     max_value=time(11, 30),
#     )
# st.write("You're scheduled for:", durationTime) # ??顯示有問題

# time_1 = datetime.datetime.strptime('05:00:00',"%H:%M:%S")
# time_2 = datetime.datetime.strptime('7:00:00',"%H:%M:%S")
# ftime1 = float(time_1)
# st.write(ftime1)

# @link [API reference — Streamlit 0.89.0 documentation](https://docs.streamlit.io/en/stable/api.html?highlight=widgets#streamlit.slider) Basic at 2021/9/26

# @link [Animate st.slider - Using Streamlit - Streamlit](https://discuss.streamlit.io/t/animate-st-slider/1441/7) at 2021/9/26
# # animate
# import streamlit as st
# import time

# slider_ph = st.empty()
# info_ph = st.empty()

# value = slider_ph.slider("slider", 0, 100, 25, 1)
# info_ph.info(value)

# if st.button('animate'):
#     for x in range(20):
#         time.sleep(.5)

#         value = slider_ph.slider("slider", 0, 100, value + 1, 1)
#         info_ph.info(value)

# @link [Streamlit Shorts: Core Functionality Series - Official Announcements - Streamlit](https://discuss.streamlit.io/t/streamlit-shorts-core-functionality-series/8248/6) 各種例子 at 2021/9/26
# datetime.datetime.strptime
# timeObj = datetime.datetime.strptime("00:05:55","%H:%M:%S")  # 轉時間物件
# created_date = timeObj.strftime("%H:%M:%S")  # 2021-09-12
# st.write(created_date)

# st.subheader("Using a python range:")
# my_range = range(1,21)
# number = st.select_slider("Choose a number", options=my_range, value=10)
# st.write('You chose %s hearts:' %number, number*":heart:")

# values = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)

# from datetime import datetime
# start_time = st.slider(
#     "When do you start?",
#     value=datetime(2020, 1, 1, 9, 30),
#     format="MM/DD/YY - hh:mm")
# st.write("Start time:", start_time)

# from datetime import time
# appointment = st.slider(
#     "Schedule your appointment:",
#     value=(time(11, 30), time(12, 45)))
# st.write("You're scheduled for:", appointment)

# start_color, end_color = st.select_slider(
#     'Select a range of color wavelength',
#     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
#     value=('red', 'blue'))
# st.write('You selected wavelengths between', start_color, 'and', end_color)


# %%
# ---[ 不重複list(letter版) ]---
import pandas as pd
words1 = "a, b"
words2 = "b, c"
# words = pd.DataFrame({"Yes": words1, "No": words2}, index=[1])
words = pd.DataFrame([["Yes", words1], ["No", words2]], columns=["Name", "Tags"])
Taglistss = ", ".join(list(words["Tags"]))
newlist = list(set(Taglistss))
# *另外一種方法: list(dict.fromkeys(preTaglist))
newlist.remove(',')
newlist.remove(' ')
newlist
# newlist = [w for w in Taglistss]
# Taglistss
# %%
