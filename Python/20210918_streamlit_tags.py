import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar

st.write("# Code for streamlit tags")

st.code(body='''
    keywords = st_tags(
    label='# Enter Keywords:', # 標題
    text='Press enter to add more' , # 內文
    value=['Zero', 'One', 'Two'], # 初始值
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], # 提示
    maxtags = 4, # 可填上限
    key='1')''',
        language="python")

maxtags = st.slider('Number of tags allowed?', 1, 10, 3, key='jfnkerrnfvikwqejn')

# 有加key，他可以暫時紀錄出過maxtags的部分耶?
keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags=maxtags,
    key="whatisthis")

st.write("### Results:")
st.write(type(keywords))

if st.button("Show"):
    st.write((keywords))

st.sidebar.write("# Code for streamlit tags sidebar")

st.sidebar.code(body='''keyword = st_tags_sidebar(
label='# Enter Keywords:',
text='Press enter to add more',
value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 
'eight', 'nine', 'three', 
'eleven', 'ten', 'four'],
maxtags = 4)''',
                language="python")

maxtags_sidebar = st.sidebar.slider('Number of tags allowed?', 1, 10, 3, key='ehikwegrjifbwreuk')


keyword = st_tags_sidebar(label='# Enter Keywords:',
                        text='Press enter to add more',
                        value=['Zero', 'One', 'Two'],
                        suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
                        maxtags=maxtags_sidebar,
                        key="afrfae")

st.sidebar.write("### Results:")
st.sidebar.write((keyword))