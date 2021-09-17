# ---
# 讀取資料夾圖片
# 分析時間並抓取網址
# 存成csv檔案
# 從csv讀取->呈現成Table
# 可選擇標題與時間點
# ---

# 將圖片檔名轉成 圖片檔名、影片名稱、標記時間、創建日期
import pathlib
import os

# from pathlib import Path

import datetime
from youtubesearchpython import VideosSearch
import streamlit as st
import pandas as pd

import shutil

# CSS
st.markdown(
    """
    <style>
    .img-time {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
        timeMM = _timeMark.split("-")[0].zfill(2)
        timeSS = _timeMark.split("-")[1].zfill(2)  # 時間補零

        # 創建日期
        _created_time = os.path.getmtime(filePath)
        _created_timeObj = datetime.datetime.fromtimestamp(_created_time)  # 轉時間物件
        created_date = _created_timeObj.strftime("%Y-%m-%d")  # 2021-09-12
        # created_time = _created_timeObj.strftime("%H%M%S")  # 214303

        return videoName, timeMM, timeSS, created_date, adjustfilePath

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
        videoName, timeMM, timeSS, created_date, adjustfilePath = setData(imgName)
        timeMark = timeMM + ":" + timeSS
        # itemOutput.extend([videoName, timeMark, created_date])
        # 確認影片名稱跟上一輪是否相同，[i-1]最開始會變成-1
        if i==0:
            prevVideoName = "None"
        else:
            prevVideoName = " ".join(folerIterlist[i-1][1].parts[-1].split(" ")[0:-2])
        print(videoName)
        print(prevVideoName)
        #?? 但原因不明 enumerate迴圈，裡面在塞enumerate應用，就會造成迴圈跑一次就停
        if videoName == prevVideoName:
            print("Same")
        else:
            print("Different")
            urlink = searchYT(videoName)
        urlinkWithTime = urlink + "#t=" + timeMM + "m" + timeSS + "s"
        itemOutput = [
            videoName,
            timeMark,
            created_date,
            urlinkWithTime,  # 之後轉alink
            urlinkWithTime,
            adjustfilePath,
        ]
        finalOutput.append(itemOutput)
        moveimg(filePath, adjustfilePath)
        print("one file done")

    # 將list轉成panda形式   
    pandaDF = pd.DataFrame(
        finalOutput,
        columns=["Name", "TimeMark", "SnapTime", "alink", "link", "FilePath"],
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
