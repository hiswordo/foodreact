# ----Scikit Basic----
# @link [Python Machine Learning Tutorial (Data Science) - YouTube](https://www.youtube.com/watch?v=7eh4d6sabA0) at 2021/9/9
# %%
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Accuracy
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# for saving and loading models
# from sklearn.externals import joblib # 已棄用
import joblib

# 決策模型圖
from sklearn import tree

# %% [markdown]
# ## ---< Import Data >---
# %%
music_data = pd.read_csv("./res/music.csv")
# music_data.shape
# music_data.describe()
# music_data.values
# build input set and output set
X = music_data.drop(columns=["genre"])
y = music_data["genre"]


# %% [markdown]
# ## ---< Learning and Predicting >---
# %%
basicModel = DecisionTreeClassifier()
basicModel.fit(X, y)
predictions = basicModel.predict([[21, 1], [22, 0]])
predictions

# %% [markdown]
# ## ---< Calculating the Accuracy >---
# 一般來說 資料的 70~80% for prediction，20~30% for testing
# ?? 那為什麼不把100%拿去train，比較準，在隨便抽樣拿來測驗呢? 應該有個公式值跟原因吧
# %%
# train_test_split會有2x2個對應tuple的數值
# test_size = 0.2 == 20% 隨機抽取資料做測驗，每次都不一樣
# 資料的多寡與乾淨程度，大程度決定了推測的結果
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
trainModel = DecisionTreeClassifier()
trainModel.fit(X_train, y_train)
predictions = trainModel.predict(X_test)
score = accuracy_score(y_test, predictions)
score

# %% [markdown]
# ## ---< Model Persistence >---
# %%
# XXX cannot import name 'joblib' : 改用 import joblib
joblib.dump(basicModel, "./res/music-recommender.joblib")
oldModel = joblib.load("./res/music-recommender.joblib")
predictions = oldModel.predict([[21, 1]])
predictions

# %% [markdown]
# ## ---< Visualizing Decision Tree >---
# %%
tree.export_graphviz(
    basicModel,
    out_file="./res/music-recommender.dot",
    feature_names=["age", "genre"],
    class_names=sorted(y.unique()),
    label="all",
    rounded=True,
    filled=True,
)

# %%
# 直接用tree作圖但畫質很差，線看不到
""" tree.plot_tree(
    basicModel,
    feature_names=["age", "genre"],
    class_names=sorted(y.unique()),
    label="all",
    rounded=True,
    filled=True,
) """
# %%
import graphviz
graphviz.Source.from_file('./res/music-recommender.dot')

# XXX ExecutableNotFound: failed to execute 'dot', make sure the Graphviz executables are on your systems' PATH
# 
# @link [How to parse a DOT file in Python](https://www.py4u.net/discuss/148304) at 2021/9/10

# %%
