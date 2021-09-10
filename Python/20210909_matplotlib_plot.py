# %%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# %%
# ---< plot 線型 >---
X = np.arange(0, 12.1, 0.1)
Y = np.sin(X)
plt.plot(X, Y, 'ko')
# plt.plot(X, Y, "--")

# Line Styles
# - '-'	solid line style
# - '--'	dashed line style
# - '-.'	dash-dot line style
# - ':'	dotted line style

# Markers
# - ^/+/, 各種符號皆有，K表黑色
# - plt.plot(X, Y, "ko")
# - plt.plot(X, Y, "ok") # k+o組合前後不計

# %%
# ---< plot 屬性 >---
plt.plot(
    X,
    Y,
    color="lime",
    linestyle="-",
    linewidth=2,
    marker=">",
    markerfacecolor="black",
    markeredgecolor="blue",
    markersize=3,
    markeredgewidth=1,
)
# plt.scatter(X, Y)  # = plt.plot(X,Y,"o")

# %% [markdown]
# ## ---< 多圖疊製 >---
# %%
plt.plot(X, Y, "-.")
ax1 = plt.gca()  # Get Current Axis
# ax1.set_title('Title here 中文問題', fontname='Taipei Sans TC Beta', fontsize=20)
ax1.set_title("Title here 中文問題", fontsize=20)
ax1.set_xlabel("Xlabel($^o$C)")  # LeteX
ax1.set_ylabel("Ylabel")

ax1.set_xticks([5, 10, 12])
ax1.set_xticklabels(["a", "b", "c"])  # 要與刻度數同量

ax1.tick_params(axis="both", direction="in", color="blue", length=10, width=3)

# %%
# ---< 多圖疊製 >---
_ = plt.plot(X, Y, "-", label="sin1", zorder=2, linewidth=5)  # 使用 _ ，若不要詳細訊息的話
_ = plt.plot(X + 2, Y, "-", label="sin2", zorder=1, linewidth=5)  # 輕鬆圖形疊加
_ = plt.legend(loc="best")  # 其他位置還有lower left之類的
# zorder不同層圖

# %%
# ---< 分圖繪製 >---
fig, ax = plt.subplots(2, 1)
# Figure(432x288) <class 'matplotlib.figure.Figure'>
# [<AxesSubplot:> <AxesSubplot:>] <class 'numpy.ndarray'>
# 指定坐標軸.plot vs plt.plot未指定座標軸
ax[0].plot(X + 2, Y, "r")
ax[1].plot(X, Y)

# 設定兩張圖同樣X軸起點，與寬度
ax[0].set_xlim([0, 10])
ax[1].set_xlim([0, 10])

# %%
# ---< 數據不同的繪製方式 >---
X2 = np.arange(1, 100, 1)
Y2 = np.exp(X2)
plt.plot(X2, Y2)
ax = plt.gca()
# 尺度的選擇
ax.set_yscale("log")

# 共用X軸，產生右邊的y座標
ax2 = ax.twinx()
ax2.plot(X, Y, "g")

# 依據右跟上座標畫出來的圖
ax3 = ax2.twiny()
ax3.plot(X, Y, "r")

# %%
# ---< 儲存圖片 >---
fig = plt.figure(figsize=(8, 4))  # 畫布比例大小，避免圖形被切被壓
plt.plot(X, Y)
plt.savefig("./res/matplot.png", dpi=400)  # dpi畫質調整

# %% [markdown]
# @link [如何使用 Matplotlib 繪製 2D 熱圖 | D棧 - Delft Stack](https://www.delftstack.com/zh-tw/howto/matplotlib/how-to-plot-a-2d-heatmap-with-matplotlib/) at 2021/9/9

# %%