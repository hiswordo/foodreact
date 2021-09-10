# ---- 20210907_pandas_csv_dataframe ----
# @link [Complete Python Pandas Data Science Tutorial! (Reading CSV/Excel files, Sorting, Filtering, Groupby) - YouTube](https://www.youtube.com/watch?v=vmEHCJofslg&t=236s) at 2021/9/7
# @link [pandas/Pandas Data Science Tutorial.ipynb at master · KeithGalli/pandas · GitHub](https://github.com/KeithGalli/pandas/blob/master/Pandas%20Data%20Science%20Tutorial.ipynb) at 2021/9/7


# ---< 讀取csv xlsx txt >---
import pandas as pd
df = pd.read_csv("./res/pokemon_data.csv")

print(df.head(3))
print(df.tail(3))
# AttributeError: module 'numpy' has no attribute 'read_csv'
# SMILE pandas寫成numpy...當然沒有read_csv的屬性
df_xlsx = pd.read_excel("./res/pokemon_data.xlsx")
df_txt = pd.read_csv("./res/pokemon_data.txt", delimiter="\t")
print(df_txt)


# ---< 選擇讀取的資料 >---
import pandas as pd
df = pd.read_csv("./res/pokemon_data.csv")

# Read Headers
print("< df.columns >", df.columns, sep="\n", end="\n--------\n") 
# Read one Column
print("< df['Name'][0:5] >", df['Name'][0:5], sep="\n", end="\n--------\n") 
# Read each Column
print("< df[['Name', 'Type 1', 'HP']] >", df[['Name', 'Type 1', 'HP']], sep="\n", end="\ n--------\n") 
# Read Each Row
print("< df.iloc[0:4] >", df.iloc[5:10], sep="\n", end="\n--------\n") 
# *Read a specific location (R,C)
print('< df.iloc[2,1] >', df.iloc[2,1], sep='\n', end='\n--------\n') 

# Row 一筆一筆分別讀出來
for index, row in df.iterrows():
    print(index, row[['Name','Type 1']], sep="\n")
""" 
0 -> indx
Name      Bulbasaur
Type 1        Grass
Name: 0, dtype: object
"""

# 兩個conditions條件時，記得要(1)&(2)才可以
print('< 尋找屬性 >', df.loc[(df['Type 1'] == "Grass") & (df['Generation'] == 1)], sep='\n', end='\n--------\n')

# %%
# ---< 資料處理 >---
import pandas as pd
df = pd.read_csv("./res/pokemon_data.csv")
# header=None的話，第0列就是原先的columns
# df2 = pd.read_csv("./res/pokemon_data.csv", header=None)
df

# %%
# 列出常用統計值結果
print("< df.describe() >", df.describe(), sep="\n", end="\n--------\n")

# Sorting/Describing Data
sortdf = df.sort_values(["Type 1", "HP"], ascending=[1, 0])
print("< sortdf >", sortdf.iloc[0:4], sep="\n", end="\n--------\n")

# Making changes to the data
# 增加
df["Total1"] = (df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"])
df["Total2"] = df.iloc[:, 4:10].sum(axis=1)  # 同樣結果
print('< df增加column"Total" >', df.head(3), sep="\n", end="\n--------\n")

# 減少
df = df.drop(columns=["Total1"])

# 重新拼湊表格
# 注意+號合併，大家要都是list[]才行，所以cols[-1]要外加[]
cols = list(df.columns)
# ['#', 'Name', 'Type 1', 'Type 2', 'Legendary', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 'Legendary']
newdf = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print("< newdf >", newdf.head(3), sep="\n", end="\n--------\n")

# ---< 資路儲存 >---
# Saving our Data (Exporting into Desired Format)
import pandas as pd
df = pd.read_csv("./res/pokemon_data.csv")

# 忽略index
df.to_csv('./res/modified.csv', index=False)
df.to_excel('./res/modified.xlsx', index=False)
df.to_csv('./res/modified.txt', index=False, sep='\t')

# ---< 資路篩選 >---
# Filtering Data
import pandas as pd
df = pd.read_csv("./res/pokemon_data.csv")

print('< df.iloc[0:2, 4:10] >', df.iloc[0:2, 4:10], sep='\n', end='\n--------\n') 
# conditions=>bool loc[bool]
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
print('< Conditions >', (df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70) , sep='\n', end='\n--------\n') 
print('< new_df >', new_df[['Name','Type 1','Type 2','HP']] , sep='\n', end='\n--------\n') 

# 重整表格index，並導出
# reset新的一欄0~4，drop前面原本的index 2,3,50...，inplace取代掉原本的new_df
new_df.reset_index(drop=True, inplace=True)
print('< new_df >', new_df, sep='\n', end='\n--------\n') 
new_df.to_csv('./res/filtered.csv')

# ---< Conditional Changes >---
import pandas as pd
df = pd.read_csv("./res/pokemon_data.csv")

dfcontains = df.loc[df['Name'].str.contains("Mega")]
print('< dfcontains >', dfcontains.iloc[0:3], sep='\n', end='\n--------\n') 

# 可以利用re來做進一步contains篩選
# ?? 使用regex好像就有很多功能了，不一定需要re，這裡只有用到re.I
import re
# dftypes = df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
dftypes = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)] # flags=re.I 忽略大小寫
print('< dftypes >', dftypes[0:3], sep='\n', end='\n--------\n') 

dftypes = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)] # flags=re.I 忽略大小寫
print('< dftypes >', dftypes[0:3], sep='\n', end='\n--------\n') 

# ---< Aggregate Statistics (Groupby) >---
import pandas as pd
df = pd.read_csv('./res/modified.csv')

# groupby 會得到一個 <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000000001DB85B0>
# 然後可以對每個群組去做運算
dfgroup = df.groupby('Type 1').mean().sort_values('Defense', ascending=False)
print('< dfgroup >', dfgroup.iloc[:,0:4], sep='\n', end='\n--------\n') 

# count是把有數值的格子當作1，空的當作0，所以大部分欄位都長的一樣，除了Type 2
# 如果你希望這個count乾乾淨淨，可以新增Count的欄位，在讓他們groupby
df['count'] = 1
dfgroup = df.groupby('Type 1').count()['count']
print('< dfgroup >', dfgroup, sep='\n', end='\n--------\n') 

dfgroupDetails = df.groupby(['Type 1','Type 2']).count()['count']
print('< dfgroupDetails >', dfgroupDetails, sep='\n', end='\n--------\n') 
# df['count'] = 1
# df.groupby(['Type 1', 'Type 2']).count()['count']

# ---< Working with large amounts of data >---
# chunksize=5 一次傳入5行
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('./res/modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
# ?? 拼接回新的dataframe，跟直接創建在新的dataframe不知道會不會有差
    new_df = pd.concat([new_df, results])

# %%
# ---< 其他 >---

# 去掉不是數位的列 remove the non-numeric columns
# ._get_numeric_data()

# pandas轉numpy
# .as_matrix()

