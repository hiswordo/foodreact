# ---
# 讀取資料夾圖片
# 分析時間並抓取網址
# 呈現成Table
# 可選擇標題與時間點
# ---

# 將圖片檔名轉成 圖片檔名、影片名稱、標記時間、創建日期
import pathlib
import os
import datetime
from youtubesearchpython import VideosSearch
import streamlit as st
import pandas as pd


# 將資料夾圖片列表，資料化，並加入csv
folder = "res/"
folderPath = pathlib.Path(__file__).parents[0].joinpath(folder)
folderIter = folderPath.iterdir()


# CSS
st.markdown(
    """
    <style>
    .img-time {
        width: 100%;
    }
    .img-container{
        margin: 2em 0em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

finalOutput = []

def itemInput(imgName):
    # 圖片檔名、影片名稱
    # imgName = "Using Pathlib in Python 6-36 screenshot.png"
    filePath = folderPath.joinpath(imgName)
    # filePath = ("./20210915_steamlit_video_bookmarks/Using Pathlib in Python 6-36 screenshot.png")
    videoNameList = imgName.split(" ")[0:-2]
    videoName = " ".join(videoNameList)  # list合併成字串

    # 標記時間
    _timeMark = imgName.split(" ")[-2]
    # timeHH = time.split("-")[0]
    timeMM = _timeMark.split("-")[0].zfill(2)
    timeSS = _timeMark.split("-")[1].zfill(2)
    timeMark = timeMM + ":" + timeSS

    # 創建日期
    # ---[ 檔案內容: 抓取創建日期 ]---
    # @link [用 Python 讀取檔案和照片的創建日期-有解無憂](https://www.uj5u.com/houduan/20962.html) at 2021/9/15
    # import time
    # ImageDate = time.ctime(os.path.getmtime(filePath)) # Sun Sep 12 21:43:03 2021

    # ! 如果是照片類: getmtime，一般類: getctime，代表創建日期
    _created_time = os.path.getmtime(filePath)  # ?? 相對檔案本身路徑耶??怎麼一下又變回來了?
    _created_timeObj = datetime.datetime.fromtimestamp(_created_time)  # 轉時間物件
    created_date = _created_timeObj.strftime("%Y-%m-%d")  # 2021-09-12
    created_time = _created_timeObj.strftime("%H%M%S")  # 214303

    # 上網並搜索 影片名稱網址、影片頻道名稱、合併 網址與標記時間
    videosSearch = VideosSearch(videoName, limit=1)
    urlink = dict(videosSearch.result()["result"][0])["link"]
    urlinkWithTime = urlink + "#t=" + timeMM + "m" + timeSS + "s"
    # print(urlinkWithTime)

    # FAIL: bs4 for youtube/google
    # from mymodules import crawler
    # searchUrl = "https://www.youtube.com/results?" + videoName.replace(" ","+")
    # soup = crawler.pageParser(searchUrl)
    # # gooLink = "https://www.google.com/search?q=youtube+Using+Pathlib+in+Python&tbm=vid"
    # links = soup.find_all("a")
    # print(links)

    itemOutput = [
        videoName,
        timeMark,
        created_date,
        urlinkWithTime,
        # "https://google.com",
        # "https://google.com",
        urlinkWithTime,
        filePath,
    ]

    finalOutput.append(itemOutput)


for ingName in folderIter:
    itemInput(ingName.parts[-1])


# Youtube 圖片、標籤時間點播放
def st_imglink(url, link=""):
    import base64

    return st.markdown(
        f"""
        <div class="img-container">
            <a target="_blank" class="img-link" href="{link}">
                <img class="img-time" src="data:image/png;base64,{base64.b64encode(open(url, "rb").read()).decode()}">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


# 將行資料apply成link
def make_clickable(link):
    return f'<a target="_blank" href="{link}">Link</a>'


# ---< Pandas: 轉html table with href link >---
# 建立df
df = pd.DataFrame(
    finalOutput, columns=["Name", "TimeMark", "SnapTime", "alink", "link", "FilePath"]
)
nameChoices = tuple(df["Name"].drop_duplicates())  # 將name整理成唯一命名
searchName = st.selectbox("Select a name", nameChoices)
# 篩選名稱
nameCondition = df["Name"] == searchName
selectedList = df.loc[nameCondition]  # .reset_index()重設index會多出一行

# 設立時間選擇上限
searchTimeMark = st.number_input(
    "give a number", min_value=0, max_value=selectedList["TimeMark"].shape[0] - 1,step=1
)

# 將link一欄，轉成可點擊href a
selectedList["alink"] = selectedList["alink"].apply(make_clickable)

# 隱藏FilePath並轉成html table
showTable = selectedList.iloc[:, 0:4].to_html(escape=False)
st.write(showTable, unsafe_allow_html=True)


# 顯示選取圖片
# ?? 為什麼本來不需要int(input number)後來又需要了呢?
st_imglink(selectedList["FilePath"].iloc[int(searchTimeMark)],selectedList["link"].iloc[int(searchTimeMark)])


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
