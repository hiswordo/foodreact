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
seriesData["a"] # 20
seriesData.b # 20
# print("seriesData.indexNamed = ", seriesData.index)
# print("< seriesData >", seriesData, sep="\n")
# print("seriesData['a'] = ", seriesData["a"]) # 20

# print("seriesData*2 = ", seriesData * 2, sep="\n")
# print("seriesData.max() = ", seriesData.max())
# print("< seriesData == 20 > ", seriesData == 20, sep="\n")

# %%
# ---< Series 資料基本處理>---
wordSeriesData = pd.Series(['Rain','Cats','and','Dogs'])
print("wordSeriesData = ", wordSeriesData, sep="\n")
print("wordSeriesData.str = ", wordSeriesData.str) # <pandas.core.strings.accessor.StringMethods object at 0...F125FD0>
print("wordSeriesData.str.cat(sep=',') = ", wordSeriesData.str.cat(sep=',')) # Rain,Cats,and,Dogs
print("wordSeriesData.str.contains('R') = ", wordSeriesData.str.contains("R"), sep="\n") # Rain,Cats,and,Dogs
print("wordSeriesData.str.contains('R') = ", wordSeriesData.str.replace("R","P"), sep="\n") # Rain,Cats,and,Dogs

# Series 其他重要運用
import pandas as pd

seriesData = pd.Series([20, 30, 40, -5, 6, 9, 10])
print("seriesData.nlargest(3) = ", seriesData.nlargest(3), sep="\n")
print("seriesData.nlargest(3) = ", seriesData.nsmallest(2), sep="\n")

# ---< DataFrame>---
# 小心loc[]是中括號，
import pandas as pd
frameDate = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
print("frameDate = ", frameDate, sep="\n")
print("frameDate.shape = ", frameDate.shape)
# 取欄
print('frameDate["Yes"] = ', frameDate["Yes"], sep="\n")
print("frameDate.iloc[0] = ", frameDate.iloc[0], sep="\n")
# loc[索引]，取列
frameDate = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]}, index=['a','b'])
print("frameDateIndex = ", frameDate, sep="\n")
print('frameDate.loc["a"] = ', frameDate.loc["a"], sep="\n") # 同iloc[0]

# 新增欄位 data["name"] = [] or Series型態
import pandas as pd
frameDate = pd.DataFrame({"Yes": [30, 30], "No": [40, 20]}, index=["村子A","村子B"])
frameDate["Both"] = [30 , 50]
#! 若有index指定名稱，下兩個須注意也要有index指定名稱，否則數值會變成NaN
frameDate["People"] = pd.Series([100, 100], index=["村子A","村子B"])
frameDate["VoteYes"] = (frameDate["Yes"]+frameDate["Both"])/frameDate["People"]
print("frameDateAdded = ", frameDate, sep="\n")

# ---< Condition操作 >---
# 利用bloon值對應其位置，達到篩選目的
# series同邏輯
import pandas as pd
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
