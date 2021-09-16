
# @link [Streamlit 超快速又輕鬆建立網頁 Dashboard – IT 空間](https://blog.jiatool.com/posts/streamlit/) at 2021/9/8

import time
import streamlit as st
import numpy as np
import pandas as pd


# ---< 網頁配置設定 >---
st.set_page_config(
    page_title="測試streamlit", # 預設:程式碼的檔名
    page_icon="random", # 可以使用 st.image 或 Emoji
    layout="centered", # "wide" or 預設:"centered"
    initial_sidebar_state="collapsed", #"expanded"，預設:"auto"(手機尺寸的設備上是隱藏，看不出差別)
)

# @link [Streamlit cheat sheet · Streamlit 官方有將 API 濃縮成一頁](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py) at 2021/9/8
# streamlit run .\20210908_streamlit\streamlit_app.py --server.port 7000
# *Run on save：程式存檔後網頁自動重跑，不需要再手動點 Rerun

# 如果想改一些設定的話
# %userprofile%/.streamlit/config.toml, creating that file if necessary:
# streamlit config show

# ---< Streamlit性質 >---
# Streamlit 只要元件有輸入值的改變，就會從上到下重新執行你的程式碼
# Jupyter筆記本一樣，一個值或一個變數名本身就會輸出到螢幕上。與Jupyter筆記本不同，方法呼叫的結果不會輸出任何東西。你必須將返回值儲存為變數才能顯示。
# xxx = st.~ 甚麼物件創立後，即可 xxx.~ 做一樣的事情

# ---< 文字顯示相關處理 >---
st.markdown("<h1 style='text-align: center; color: red;'>Title Comes</h1>", unsafe_allow_html=True)
st.title('我的第一個應用程式')
newdiv = st.empty()
myTiming = "4:30"
newdiv.text(f'Show {myTiming}')
"""123\n
456"""

# ---< Magic Commands >---
st.write("## 嘗試創建**表格**：")

# 表格
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}, index=['a','b','c','d'])
df

# Numpy + st折線圖 + st確認框
ckwd = st.checkbox('測試checkbox')
ckwd # bool
if st.checkbox('顯示折線圖'):
    chart_data = pd.DataFrame(
        np.random.randint(1,30,size=[20,3]),
        columns=['a', 'b', 'c'])
    # chart_data
    st.line_chart(chart_data)

# *Numpy + st圖表和地圖 + st選擇盒
# 台灣(lat,lon)=()~鼻頭里[25.120810, 121.913623], 松江南京: 25.0524242,121.5299078

# *直接顯示文字
""" 
KC = 愛河之心[22.6519787,120.3179018] \n
TP = 松江南京 [25.0524,121.52990] \n
TC = 草衙道 [24.1453248,120.6644667] \n
"""
KC = [22.6519,120.3179]
TP = [25.0524,121.52]
TC = [24.1453,120.6644]
selectedLocName = {'高雄':KC , '台北':TP, '台中':TC}
selected = st.selectbox(
    '以哪個地點為中心？',
    ['高雄', '台北', '台中']) 

map_data = pd.DataFrame(
    # 以selected為中心，除[80,80]的密度分布，去常態分佈
    np.random.randn(100, 2) / [80, 80] + selectedLocName[selected],
    columns=['lat', 'lon'])
st.map(map_data)

# *randn()的意義
# Return a sample (or samples) from the “standard normal” distribution.
# np.random.randn(R, C)
# sigma * np.random.randn(...) + mu

# ---< 調整佈局 >---
# st 側邊框
# Ex: st.sidebar.markdown(), st.sidebar.slider(), st.sidebar.line_chart().
option = st.sidebar.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
'你的答案：', option


left_column, middle_column, right_column = st.columns(3)
pressedbtn = middle_column.button('Press me?')
pressedbtn # bool
if pressedbtn:
    middle_column.write("Woohoo!")

expander = st.expander("點擊來展開...")
expander.write("Here you could put in some really, really long explanations...")


# ---< 加入進度條 >---
import time

pbtn = st.button('Progress')

# bar2 = st.progress(150)
# bar2
def progressbar():
    # Add a placeholder
    latest_iteration = st.empty()
    showmsg = st.empty()
    showmsg.text('Starting a long computation...')
    # 如果設定bar的進度條為0，如果直接st.progress跑循環，會跑出100個bar
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'# Iteration # {i+1}')
        bar.progress(i + 1)
        time.sleep(0.02)
    # 上面跑完，下面才會顯示
    showmsg.text('...and now we\'re done!' )

if pbtn:
    progressbar()

# ---< 使用快取 >---
# 使用 @st.cache 裝飾器，將之前運算過的結果快取起來，就能直接使用之前的結果
# 要使用 @st.cache 裝飾器，就需要將運算部分的程式碼包成函式(def)。
# 如果沒有使用的話，你會發現，每次拉一次都要等兩秒
# ?? 不過我比較納悶的是，所以不需要特別寫，每拉一次新的數值輸入有快取就會跳過中間所有過程嗎?
@st.cache(suppress_st_warning=True)
def expensive_computation(a):
    st.write(f"沒有快取：expensive_computation({a})")
    time.sleep(2)
    return a * 2

a = st.slider("選擇一個數字", 0, 10)
result = expensive_computation(a)
st.write("結果：", result)


# 嘗試: 隨機float-10~11
# outcome = np.random.randint(-10,11,[10,2])*np.random.random([10,2])

# ---< 放圖片 >---
# 基本型
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Antalya-Alanaya_aras%C4%B1_t%C3%BCnel.jpg/800px-Antalya-Alanaya_aras%C4%B1_t%C3%BCnel.jpg")
# st.image(image, width=64)

# 基本markdown
md = """
![Tunnels](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Antalya-Alanaya_aras%C4%B1_t%C3%BCnel.jpg/800px-Antalya-Alanaya_aras%C4%B1_t%C3%BCnel.jpg)
"""
st.markdown(md)

# Href on image
st.markdown('''
    <a href="https://docs.streamlit.io">
        <img src="https://media.tenor.com/images/ac3316998c5a2958f0ee8dfe577d5281/tenor.gif" />
    </a>''',
    unsafe_allow_html=True
)


# 進階markdown 本地圖片
import base64
LOGO_IMAGE = "xxx.png"

# ---< 插入CSS >---
st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
    }
    .logo-img {
        float:right;
        width: 60%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# @link [Using Images - Streamlitopedia](https://pmbaumgartner.github.io/streamlitopedia/sizing-and-images.html) at 2021/9/15
# @link [Cache版本 Href on image - Using Streamlit - Streamlit](https://discuss.streamlit.io/t/href-on-image/9693/3) at 2021/9/15
st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">Logo Much ?</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 包裝成def
def st_img(url):
    import base64
    return st.markdown(
        f"""
        <div class="container">
            <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(url, "rb").read()).decode()}">
            <p class="logo-text">Logo Much ?</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st_img(filePath)

# @link [GitHub - asehmi/fastapi-wrapper-apiness: CLI and Streamlit applications to create APIs from Excel data files within seconds, using FastAPI](https://github.com/asehmi/fastapi-wrapper-apiness) at 2021/9/15
# 輪番，尚未測試
if st.sidebar.checkbox('Readme', False):
    st.markdown('---')
    '''
    ### Readme :smile:
    '''
    with open('./README.md', 'r', encoding='utf-8') as f:
        readme_lines = f.readlines()
        readme_buffer = []
        images = [
            'https://picsum.photos/350/200?random=1',
            'https://picsum.photos/350/200?random=2',
            'https://picsum.photos/350/200?random=3',
            'https://picsum.photos/350/200?random=4',
            'https://picsum.photos/350/200?random=5',
            'https://picsum.photos/350/200?random=6',
            'https://picsum.photos/350/200?random=7',
            'https://picsum.photos/350/200?random=8',
            'https://picsum.photos/350/200?random=9'
            'images/apiness.png',
            'images/fastapi_testimonial.png'
        ]
        for line in readme_lines:
            readme_buffer.append(line)
            for image in images:
                if image in line:
                    st.markdown(' '.join(readme_buffer[:-1]))
                    st.image(f'https://raw.githubusercontent.com/asehmi/fastapi-wrapper-apiness/main/{image}')
                    readme_buffer.clear()
        st.markdown(' '.join(readme_buffer))

# 測試中
# localPath = "file:///G:/my_coding/Python/20210915_steamlit_video_bookmarks/Using%20Pathlib%20in%20Python%206-36%20screenshot.png"
# localPath = "G:/my_coding/Python/20210915_steamlit_video_bookmarks/Using%20Pathlib%20in%20Python%206-36%20screenshot.png"
import base64
st.markdown(
    f"[![{filePath}]](https://www.youtube.com/watch?v=Egj_DdGUIDI)")
st.image(base64.b64encode(open(filePath, "rb").read()))

# ---[ streamlit: 自定義樣板 ]---
def my_widget(key):
    st.subheader('Hello there!')
    return st.button("Click me " + key)
# This works in the main area

clicked = my_widget("first")

# And within an expander
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("second")

# AND in st.sidebar!
with st.sidebar:
    clicked = my_widget("third")

# ---[ Pandas: 轉html table with href link ]---
df = pd.DataFrame({"Yes": [30, 30], "No": ["html=7", "html=6"]}, index=["村子A", "村子B"])
def make_clickable(link):
    # Link另開視窗 # target="_blank"
    # extract clickable text to display for your link
    # text = link.split('=')[1]
    return f'<a href="{link}">Link</a>'

# link is the column with hyperlinks
df["No"] = df["No"].apply(make_clickable)
st.write(df.to_html(escape=False), unsafe_allow_html=True)




