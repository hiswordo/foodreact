# ---- Pandas ----
# @link [Python Pandas 資料分析 - Series 單維度資料 By 彭彭 - YouTube](https://www.youtube.com/watch?v=175ZZC3Hr0Y&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=26) at 2021/9/7
# 大部分與python相同

# %%
# ---< Series >---
import pandas as pd

seriesData = pd.Series([20, 30, 40])
print("seriesData = ", seriesData, sep="\n")
print("seriesData.size = ", seriesData.size)
print("seriesData.indexBasic = ", seriesData.index)  # RangeIndex(start=0, stop=3, step=1) 代表一般的資料索引0 1 2

# %%
# 建立index
# ! index數量要跟資料一致
# ! 如果用數字當索引，此時不能再用順序索引
seriesData = pd.Series([20, 30, 40], index=[2, 7, 8]) # seriesData.indexNamed =  Int64Index([7, 8, 9], dtype='int64') 
seriesData = pd.Series([20, 30, 40], index=['a','b','c']) #!Index(['a', 'b', 'c'], dtype='object' <= object指的是字串
seriesData.index

# %%
seriesData["a"] # 20

# %%
seriesData.b # 30

# %%
seriesData * 2

# %%
seriesData.max()

# %%
seriesData == 20

# %%
# ---< Series 資料基本處理>---
wordSeriesData = pd.Series(['Rain','Cats','and','Dogs'])
print("wordSeriesData = ", wordSeriesData, sep="\n")
print("wordSeriesData.str = ", wordSeriesData.str) # <pandas.core.strings.accessor.StringMethods object at 0...F125FD0>

# %%
# ---< Series str處理 >---
print("wordSeriesData.str.cat(sep=',') = ", wordSeriesData.str.cat(sep=',')) # Rain,Cats,and,Dogs
print("wordSeriesData.str.contains('R') = ", wordSeriesData.str.contains("R"), sep="\n") # Rain,Cats,and,Dogs
print("wordSeriesData.str.contains('R') = ", wordSeriesData.str.replace("R","P"), sep="\n") # Rain,Cats,and,Dogs

# %%
# Series 前幾大，前幾小，最大，最小值
seriesData = pd.Series([20, 30, 40, -5, 6, 9, 10])
print("seriesData.nlargest(3) = ", seriesData.nlargest(3), sep="\n")
print("seriesData.nlargest(3) = ", seriesData.nsmallest(2), sep="\n")

# %%
# ---< DataFrame>---
# 字典傳入，定義每一欄
frameDate = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
print("frameDate = ", frameDate, sep="\n")
print("frameDate.shape = ", frameDate.shape)

# %%
# ---< DataFrame 取行或列(可運算) >---
# [label]、iloc()取欄
print('frameDate["Yes"] = ', frameDate["Yes"], sep="\n")
print("frameDate.iloc[0] = ", frameDate.iloc[0], sep="\n")
# iloc[R,C]
frameDate.iloc[:,1] # 列全要，行取1
frameDate.iloc[1,:] # 列取1，行全要

# %%
# loc[索引]、loc[label]，取列
# 小心loc[]用的是中括號，非()
frameDate.index = ['a','b'] # 定義列的label
print("frameDateIndex = ", frameDate, sep="\n")
print('frameDate.loc["a"] = ', frameDate.loc["a"], sep="\n") # 同iloc[0]

# %%
# 新增欄位 data["name"] = [] or Series型態
frameDate = pd.DataFrame({"Yes": [30, 30], "No": [40, 20]}, index=["村子A","村子B"])
frameDate["Both"] = [30 , 50]
#! 若有index指定名稱，下兩個須注意也要有index指定名稱，否則數值會變成NaN
frameDate["People"] = pd.Series([100, 100], index=["村子A","村子B"])
frameDate["VoteYes"] = (frameDate["Yes"]+frameDate["Both"])/frameDate["People"]
print("frameDateAdded = ", frameDate, sep="\n")

# %%
# ---< Condition操作 >---
# 利用`bool`值對應其位置，達到篩選目的
# series同邏輯
data = pd.DataFrame({
    "name":["Amy", "Henry", "Tom"],
    "salary":[30000, 28000, 50000]
})
print('原本date = ', data, sep='\n')
condition = [True, False, True]
print('取一、三列 = ', data[condition], sep='\n')
condition = data["salary"] > 40000
print('取薪水大於4w那一列 = ', data[condition], sep='\n')
condition = data["name"].str.contains("m")
print('取名字包含m的', data[condition], sep='\n')

# %%
