import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

# Web scraping of NBA player stats
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0) # <class 'list'>
    raw = html[0] # <class 'pandas.core.frame.DataFrame'>
    # df = html[0]
    # raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    # raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

# Sidebar - Team selection
# unique()後得到array(['VAN', 'DEN',...], dtype=object)
sorted_unique_team = sorted(playerstats.Tm.unique())
# multiselect(名稱, 輸入, 預設值)
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
if st.button('Download'):
    df_selected_team.to_csv('C:/Users/oEdward/Downloads/playerstats.csv',index=False)

# ?? 瀏覽器檔案下載，目前還不會用
# def filedownload(df):
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
#     href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
#     return href

# st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# @link [【Python】繪製熱力圖seaborn.heatmap，cmap設置顏色的參數_小白兔de窩-CSDN博客_cmap](https://blog.csdn.net/ztf312/article/details/102474190) at 2021/9/9
# @link [Seaborn（sns）官方文檔學習筆記（第一章 藝術化的圖表控制） - 知乎](https://zhuanlan.zhihu.com/p/27435863) at 2021/9/9
# Seaborn Heatmap
# if st.button('Intercorrelation Heatmap'):
st.header('Intercorrelation Matrix Heatmap')
# df_selected_team.to_csv('output.csv',index=False)
df = pd.read_csv('output.csv')
corr = df.corr() # 欄位相關性表
# 反正另外一半三角形是重複的，用mask遮起來
mask = np.zeros_like(corr) # 創造同長寬的0矩陣
# [1 1]
# [0 1] 像是這樣的三角形矩陣  
mask[np.triu_indices_from(mask)] = True

# ?? 全域設定樣式，詳細影響不知，效果跟with相同
# fig = plt.figure(figsize=(7,5)) 
# sns.set_style("white")
# ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)

# *全域設定樣式 sns.set_style("whitegrid")
# *臨時設定圖形樣式 with sns.axes_style(...) 只有with區塊有作用
# darkgrid 黑色網格（預設）
# whitegrid 白色網格
# dark 黑色背景
# white 白色背景
# ticks 應該是四周都有刻度線的白背景？

with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5)) # 設置圖片尺寸
    ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)

# 202012 pyplot 應使用參數，可以先忽略警告用以下
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# %%
