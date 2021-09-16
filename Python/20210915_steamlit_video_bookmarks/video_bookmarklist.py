import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import json
import csv

import pandas as pd

""" filename = "./20210915_steamlit_json/videos_df.json"
with open(filename, "r") as read_file:
    # data = json.load(read_file) # dict
    data = pd.read_json(filename, orient="index") # pd
"""
"""
asba:
    # 註解複製格式
    冒號 + 井字 + Tab
"""

filename = "./20210915_steamlit_json/videos_df.csv"
df = pd.read_csv(filename)

# csv 寫入、newline=''每次寫入不空一行
def addrow(name, age):
    with open(filename, "a", newline='') as f:
        add_row = csv.writer(f)
        data_row = [name, age]
        add_row.writerow(data_row)

name = st.text_input("Enter Name","Name")
age = st.number_input("Enter Age", min_value=18, max_value=88, step=2)
if st.button("Input"):
    addrow(name, age)

# !一但有一列，行數不對就會爆掉了
df = pd.read_csv(filename)
st.write(df.sort_index(ascending=False))

st.header("Youtube")

