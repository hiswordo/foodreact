import streamlit as st

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

# ---[設定steamlit基本設定:要放在最開始]---
menu_items = {
	# 'Get help': 'https://www.google.com/',
	# 'Report a bug': '',
	'About': '''
    ## My Custom App

    Some markdown to show in the About dialog. right?
	''',
}

# st.set_page_config(layout="wide")
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    # page_icon="🧊",
    layout="wide",
    # initial_sidebar_state="expanded",
    # initial_sidebar_state="auto",
    menu_items=menu_items,
)

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


xlsxfileName = "./20210915_steamlit_video_bookmarks/modified.xlsx"

if st.sidebar.checkbox("讀取excel資料庫", True):
    # # 讀取，記得用read_excel
    df = pd.read_excel(xlsxfileName)  # , index=False)  # encoding="utf-8"

# 顯示excel所有資料，測試用
st.dataframe(df)



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

# CSS
# 圖片連結: img-time、影片iframe: vidoeo-container
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Noto+Sans&display=swap');
    /*@media (min-width: 300px) {.wrap{width: 480px;}}
    @media (min-width: 600px) {.wrap{width: 680px;}}*/
    @media (min-width: 1275px) {.card{width: 28vw; height: 16.875vw;}}
    @media (min-width: 1645px) {.card{width: 370px; height: 207px;}}
    body {
        /*background:#ccc;
        color #000;*/
        font-family: 'Noto Sans', sans-serif;
    }

    .card{
        /* 文字樣式 */
        font-size: 5rem;
        color: #333;
        -webkit-text-stroke: 2px #999;

        /* flex屬性內部中央:這邊影響文字 */
        justify-content: center;
        align-items: center;

        /* 卡片1280x720 */
        /*width: 20vw;
        height: 11.25vw;
        width: 370px;
        height: 207px;*/
        display: flex;
        border: 1px solid #000;
        border-radius: 10px;
        margin: 2vh auto;
    }

    .card{transform:scale(1,1); transition: all 0.5s ease-out;}
    .card:hover{
        transform:scale(2,2);
        z-index:3;
    }

    .animated-grid{
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        /*display: -webkit-flex;*/

        --card-delay: 100ms;
    }

    @keyframes showUpCard {
        0% {
            opacity: 0;
            transform: scale(1,0);
            filter: hue-rotate(90deg);
        }
        100% {
            opacity: 1;
            transform: scale(1,1);
            filter: hue-rotate(0deg);
        }
    }
    .card {
        /* animation: showUpCard 1s 0s ease-out; */
        animation-name: showUpCard;
        animation-duration: 1s;
        /*forward停留動畫最後結果，或是backwards停留在html初始狀態*/
        animation-fill-mode: backwards;
        transition-timing-function: cubic-bezier(0.39, 0.575, 0.565, 1);
    }

    .card{animation-delay: calc(1 * var(--card-delay));}
    </style>
    """,
    unsafe_allow_html=True,
)

def imgalink(url, link=""):
    import base64
    showimg = f"""
        <a class="card" target="_blank" class="img-link" href={link}> 
            <img src="data:image/png;base64,{base64.b64encode(open(url, "rb").read()).decode()}">
        </a>
        """
    return showimg

import base64
def imgbase(url):
    imgbase64 = base64.b64encode(open(url, "rb").read()).decode()
    return imgbase64

# ---[ streamlit 使用當地圖片 ]---
from PIL import Image

def showimgs():
    imgShowlink = []
    imgTimelink = []
    imglist = []
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
        
        image = Image.open(imgurl)
        imglist.append(st.image(image, caption=imgurlWithTime))
    return imgTimelink, imgShowlink
        # st.image(image, caption='Sunrise by the mountains',use_column_width=True)
        # print(str(imgurl))
        # indices_on_page, images_on_page = map(list, zip(*image_iterator))
        # st.image(str(imgurl), width=100, caption=indices_on_page)
        # st.image(str(imgurl), width=100)
        # st.image(str(imgurl))

imgTimelink, imgShowlink = showimgs()

# print(str(pathlib.Path(df.loc[condition, "FilePath"].values[0])))
# st.image(str(pathlib.Path(df.loc[condition, "FilePath"].values[0])))
onelinktest = Image.open(imgShowlink[0]) # <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=1280x720 at 0x325092E0>
oneimgbase = imgbase(imgShowlink[0]) # base64
twoimgbase = imgbase(imgShowlink[1]) # base64

# 方法

iframediv = '''
            <iframe style="z-index:1;" id="ytplayer" type="text/html" src="https://www.youtube.com/embed/xS5Lv7-bMYI#t=06m39s" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="0">
            </iframe>
        '''
            
def showalinkimgs():
    liliimg = []
    for i in range(df.loc[condition].shape[0]):
        liliimg.append(f'''<a class="card imghover" style="z-index:3; background-image: url('data:image/png;base64,{imgbase(imgShowlink[i])}'); background-size: cover;">{iframediv}</a>''')
    imgNextlines = "\n\t\t\t".join(liliimg)
    return imgNextlines
# print(onelinktest)
# print(oneimgbase)

st.markdown(
    f"""
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" href="animated-grid.css">
    </head>
    <body>
        <div class="animated-grid">
            {showalinkimgs()}
        </div>
        
    </body>
    """,
    unsafe_allow_html=True,
)


# @link [Grid of images with the same height? - Using Streamlit - Streamlit](https://discuss.streamlit.io/t/grid-of-images-with-the-same-height/10668/7) at 2021/10/1
import streamlit as st
from itertools import cycle

filteredImages = imgShowlink # your images here
caption = imgTimelink # your caption here
cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(filteredImages):
    showimglink = Image.open(filteredImage)
    next(cols).image(showimglink, width=300, caption=caption[idx])

# sunset_imgs = [
#     'https://unsplash.com/photos/-IMlv9Jlb24/download?force=true',
#     'https://unsplash.com/photos/ESEnXckWlLY/download?force=true',
#     'https://unsplash.com/photos/mOcdke2ZQoE/download?force=true',
#     'https://unsplash.com/photos/GPPAjJicemU/download?force=true',
#     'https://unsplash.com/photos/JFeOy62yjXk/download?force=true',
#     'https://unsplash.com/photos/kEgJVDkQkbU/download?force=true',
#     'https://unsplash.com/photos/i9Q9bc-WgfE/download?force=true',
#     'https://unsplash.com/photos/tIL1v1jSoaY/download?force=true',
#     'https://unsplash.com/photos/-G3rw6Y02D0/download?force=true',
#     'https://unsplash.com/photos/xP_AGmeEa6s/download?force=true',
#     'https://unsplash.com/photos/4iTVoGYY7bM/download?force=true',
#     'https://unsplash.com/photos/mBQIfKlvowM/download?force=true',
#     'https://unsplash.com/photos/A-11N8ItHZo/download?force=true',
#     'https://unsplash.com/photos/kOqBCFsGTs8/download?force=true',
#     'https://unsplash.com/photos/8DMuvdp-vso/download?force=true'
# ]
# image_iterator = paginator("Select a sunset page", sunset_imgs)
# indices_on_page, images_on_page = map(list, zip(*image_iterator))
# st.image(images_on_page, width=100, caption=indices_on_page)


# %%
lili = ['1','2','3','4']
"\n".join(lili)
# print("\n".join(lili))

def showup():
    lili = ['1','2','3','4']
    return "\n\t\t\t".join(lili)

newpost = f'''
    abc
    {showup()}
'''
# print(newpost)
# a_list = ["a", "b", "c"]
# joined_string = "\n".join(a_list)
# print(joined_string)
# %%
