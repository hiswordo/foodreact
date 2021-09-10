# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% [markdown]
# ---- 20210907_pandas_csv_dataframe ----
# @link [Complete Python Pandas Data Science Tutorial! (Reading CSV/Excel files, Sorting, Filtering, Groupby) - YouTube](https://www.youtube.com/watch?v=vmEHCJofslg&t=236s) at 2021/9/7
# %% [markdown]
# <div class="alert alert-info">
#   <strong>Let's start with THIS blue box:</strong>
# </div>

# %%
import pandas as pd
import numpy as np
df = pd.read_csv("./res/pokemon_data.csv")
dfc = df.corr()
mask = np.zeros_like(dfc)
mask[np.triu_indices_from()]

# %%
df.head(5)[df.columns[1:3]]


# %%
df.tail(5)


# %%
df.columns


# %%
df['Name'][0:5]


# %%
df[['Name', 'Type 1', 'HP']][10:15]

# %% [markdown]
# 取5~9列

# %%
df.iloc[5:10]


# %%
df.iloc[2,1]

# %% [markdown]
# 兩個conditions條件時，記得要(1)&(2)才可以

# %%
df.loc[(df['Type 1'] == "Grass") & (df['Generation'] == 1)]

# %% [markdown]
# Type 1 ascending
# HP descending

# %%
df.sort_values(["Type 1", "HP"], ascending=[1, 0])


# %%
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
df.tail(3)


# %%
# .drop新資料刪除欄跟列
df = df.drop(columns=['Total'])
df = df.drop(index=[797,799])
df.tail(3)


# %%
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# ^一直重複執行也不會跑出第二個Total的，欄的名稱唯一
df.head(3)


# %%
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]][0:4]
df


# %%
df = pd.read_csv("./res/pokemon_data.csv")
for index, row in df.iloc[1:5].iterrows():
    print(index, row[['Name','Type 1']], sep="\n")


# %%
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.reset_index(drop=True, inplace=True)
print('< new_df >', new_df, sep='\n', end='\n--------\n') 

# %%
