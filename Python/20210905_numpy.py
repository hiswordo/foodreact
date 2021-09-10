# ---- Numpy ----
# @link 比較完整，但例子都比較難一點，不太解釋 [# @link [Lec02 Python Numpy - YouTube](https://www.youtube.com/watch?v=EtIz7bgAUW4&list=PLj6E8qlqmkFv1rlU7BGntOGe_RFnrv9Ip&index=27) at 2021/9/6
# @link 講得很慢 但還蠻完整的 [Python NumPy 入門教學、快速開始 By 彭彭 - YouTube](https://www.youtube.com/watch?v=nJUMpIo5rmg&list=PL-g0fdC5RMboq4yOQmvwYXamPDL4uZYEL) at 2021/9/5
# 這講者外積都分不清楚...
""" 
陣列 代替 列表處理資料
Panda & TensorFlow 的基礎 
"""
# %%
import numpy as np

# ---- 一維陣列 ----
# %%
# *Creating from ragged nested sequences (list-or-tuple ndarrays with different lengths or shapes) is deprecated
# *you must specify 'dtype=object' when creating the ndarray. unlike array([3, [4], '5'])
# 可以放入list或tuple
ndarray = np.array([3, 4, 5])
res = np.char.mod('%d', ndarray) # array(['3', '4', '5'], dtype='<U1')
ndarray
res 

# %%
ndarrayEmpty = np.empty(3)  # 未指定
nd0s, nd1s, nd1to10 = np.zeros(3), np.ones(3), np.arange(10)

print(f"{ndarray = }")
print(f"{ndarray.size = }")
print(f"{ndarray.ndim = }")
print(f"{ndarray.dtype = }") #?? 會自動調整成一致的，345 or '3''4''5'，int32 or <u1
print(f"{ndarrayEmpty = }")  # clr: 記憶體本來的位置 [4.86932125e-95 3.19115799e-90 2.09135757e-85]
print(f"{nd0s = }, {nd1s = }, {nd1to10 = }")  # ?? 利用format的方式列印，會多一個逗號不用管? nd0=array([0., 0., 0.])

# ---- 二維陣列以上----
# *技巧1: 每經過一個框，由外而內看逗號或空格即可，[沒逗號代表1]，[1個逗號,代表2] 也等於包起來的資料拉
# *技巧2: 輸入的時候，可以忽略最外面的紅色[]，會比較好想
# *技巧3: 直到逗號前，連續離開幾個框，也要補上連續幾個框(跳幾階的概念)

# ---< 3x2矩陣 >---
ndarrayTwo = np.array([[1,2],[3,4],[5,6]]) 
""" 
    [
        [1, 2], 
        [3, 4], 
        [5, 6]
    ]
 """
nd0arrayTwo = np.zeros([3,2])

# ---< 2x2x3矩陣 >---
# import numpy as np
ndarrayThree = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,1,2]]])
# print(f'{ndarrayThree.sum(axis=0) = }')
""" 
    [
        [
            [1,2,3],
            [4,5,6]
        ],
        [
            [7,8,9],
            [0,1,2]
        ]
    ]
 """
nd0arrayThree = np.zeros([2,2,3]) # 2x2x3總共12個資料
print(f'{ndarrayTwo = }')
print(f'{nd0arrayTwo = }')
print(f'{ndarrayThree = }')
print(f'{nd0arrayThree.size = }')

# ---- 1. 逐元運算 (element-wise)(+-*/) ----
# 算術 比較 矩陣 統計
import numpy as np
nd001 = np.array([1,3,5])
nd002 = np.array([2,4,6])
print(f'{nd001*3 = }')
print(f'{nd001*nd002 = }')
print(f'{np.multiply(nd001, nd002) = }') # 同上乘法 # 元素乘積（element-wise product）
print(f'{nd001>nd002 = }')
print(f'{nd001==3 = }')
print(f'{nd002<6 = }')

# 內積的三種寫法
print(f'{nd001@nd002 = }')
print(f'{np.dot(nd001,nd002) = }')
print(f'{np.inner(nd001,nd002) = }')

# 外積
# !補充: 而Exterior Product是解析幾何中的外積(WikiPedia: Exterior Algebra)，又叫叉乘(WikiPedia: Cross Product)
print(f'{np.cross(nd001,nd002) = }')

# 全部相乘 1x3個資料 x 1x3個資料=9個資料
# !補充: Outer Product是線性代數中的外積(WikiPedia: Outer Product)。也就是張量積 
print(f'{np.outer(nd001,nd002) = }')

""" 
3. 統計運算
3.1 總和 (sum)
3.2 逐值累加 (cumsum)
3.3 最大最小值 (max, min)
3.4 平均數 (mean)
3.5 標準差 (std) 
"""
import numpy as np
nd003 = np.array([[1,3,5],[2,4,6]])
print(f'{nd003.sum() = }')
# axis全部統計都可以用
# ?? axis的判別，第N個維度，可以對應都可以，萬一沒對應不知道會怎樣?
# *從外面往內看，逗號看成加號即可
print(f'{nd003.sum(axis=0) = }') # *行加總 = 第一維度相加
print(f'{nd003.sum(axis=1) = }') # *列加總 = 第二維度相加
print(f'{nd003.cumsum() = }') # nd003.cumsum() = array([ 1,  4,  9, 11, 15, 21], dtype=int32)
# 更改資料
nd003[1,2]=15
print(f'{nd003 = }')

# ---- reshape 維度、形狀操作 ----
# *產生新的array
# 查型 轉置 扁平 重朔
import numpy as np
nds001 = np.array([[1,3,5],[2,4,6]]) # 2x3=6筆資料
print(f'{nds001.shape = }')
print(f'{nds001.T = }')
print(f'{nds001.T.shape = }')
print(f'{nds001.ravel() = }')
print(f'{nds001.reshape(6,1) = }') # 重朔反正就是會從頭數下去，直到數完資料
print(f'{nds001.reshape(-1,2) = }') # *-1代表讓他自己配置，根據二維2代表:2行，前面一維-1代表6/2得到3列
print(f'{nds001.reshape(3,2) = }') # 等同於上
""" array([[1, 3],
            [5, 2],
            [4, 6]]) """

# 如果要更改原矩陣，要用.resize

# 簡單綜合應用
nds002 = np.arange(10,28,2).reshape(3,3).sum(axis=1)
print(f'{nds002 = }')

# ---- 多維陣列 ndarray 取值、索引、切片操作、...、真假值操作 ----
# *索引與切片與python list操作皆相同
# 多維度，只是變成[1,2,3維度]的概念，可以用成[1:2,0:1,1]之類的方式
import numpy as np
ndsli001 = np.array([[[3,2,1],[0,7,5]],[[6,8,2],[3,1,0]]]) # 2x2x3 矩陣
print(f'{ndsli001.shape = }')
print(f'{ndsli001[0,1,1] = }') # 7
print(f'{ndsli001[1,0:2,0:2] = }') # 1x2x2=四筆資料 array([[6, 8],[3, 1]])
# *注意雖然取出來的意思一樣，但2:3回傳的[]
print(f'{ndsli001[1,1,2] = }') # 0
print(f'{ndsli001[1,1,2:3] = }') # array([0])
""" ndsli002 = np.array([[x for x in range(1,11,2)],[x for x in range(2,11,2)]]) # 好玩
print(f'{ndsli002 = }')
print(f'{ndsli001[0,::2] = }') # ?? """

# ...全都要，比:，直接表達剩餘全部
print(f'{ndsli001[0,...] = }') # array([[3, 2, 1],[0, 7, 5]])
print(f'{ndsli001[...,1,1:3] = }') # array([[7, 5],[1, 0]])

# *取出特定位置index的值
# 拿`1`一維全部，`1`二維第二個，`[0,2]`三維第1跟第3個
import numpy as np
ndsli001 = np.array([[[3,2,1],[0,7,5]],[[6,8,2],[3,1,0]]]) # 2x2x3 矩陣
print(f'{ndsli001[:,1,[0,2]] = }') # array([[0, 5],[3, 0]])
print(f'{ndsli001[:,[0,1],[0,2]] = }') # *[X1,Y1],[X2,Y2]，配對的意思，取(0,0)，跟(1,2)

# *進階: 可以用bloon值決定哪些要輸出
# 取出偶數的資料
mask = ndsli001 % 2 == 0
print(f'{mask = }')
print(f'{ndsli001[mask] = }')

# ?? 取出非0值
# print(f'{ndsli001.nonzero() = }')
# ?? 搭配
# print(f'{(ndsli001>3).nonzero() = }')

# ---- 多維陣列 ndarray 合併操作 切割操作 ----
# *同維同量
# 小心裡面還有一個括號 vstack((array1,array2))
import numpy as np
nd001 = np.array([1,3,5]) # 1x3
nd002 = np.array([2,4,6]) # 1x3
vResult = np.vstack((nd001,nd002)) # 2x3 一維合併，二維不動
hResult = np.hstack((nd001,nd002)) # 1x6 一維不動，二維合併
print(f'{vResult = }') # array([[1, 3, 5],[2, 4, 6]])
print(f'{hResult = }') # array([1, 3, 5, 2, 4, 6])
nd003 = np.array([9,9]) # 1x2
h3Result = np.hstack((nd001,nd002,nd003)) # 1x8
print(f'{h3Result = }')
# 此時，vstack就不能三者合併，因為二維數據並不相同
# // v3Result = np.vstack((nd001,nd002,nd003))

# 切割操作，相同邏輯
# *切成很多array的概念
# *N維切，由1維開始，垂數橫切，平數直切
import numpy as np
ndk001 = np.array([[1,2,3,4],[7,0,5,9]]) # 2x4
print(f'{np.vsplit(ndk001,2) = }') # 1x4跟1x4 : 一維切"2"份，二維不動
""" [array([[1, 2, 3, 4]]), array([[7, 0, 5, 9]])] """
print(f'{np.hsplit(ndk001,2) = }') # 2x2跟2x2 : 一維不動，二維切成"2"份
"""[array([[1, 2],[7, 0]]), 
    array([[3, 4],[5, 9]])] """
print(f'{np.hsplit(ndk001,4) = }') # 一維不動，二維切成"4"份

# *進階:使用split相切
import numpy as np
mat = np.random.randint(1,6,size=(3,12))
# *中間indices_or_sections為切割點的意思
# ?? 特別的是從0當切割點，還會切出本來的性質"array([], shape=(0, 12), dtype=int32)"
matspv = np.split(mat,[0,2],axis=0) # *一維切割，array[0]=性質 0 array[1]=第0~1列 2 array[2]=第2~剩下
print(f'{mat = }')
print(f'{matspv = }')
print(f'{matspv[2] = }')
matsph = np.split(mat,[3,4,7],axis=1) # 二維切割，array[0]=第0~2行 3 array[1]=第3行 4 array[2]=第4~6行 7 array[3]=7~剩下 
print(f'{matsph = }')
print(f'{matsph[1] = }')

# ----其他操作補充----
# 搭配數學值放前面，sqrt、sum、max、log... # ?? 裡面放[] or Array都可以的樣子
import numpy as np
import math
ndegree = [30,60,90]
nradian = [math.radians(x) for x in ndegree]
ndn = np.array(nradian)
print(f'{ndn = }')
print(f'{np.sin(ndn) = }') # [0.5       0.8660254 1.       ]
print(f'{np.cos(ndn) = }') # ?? 為啥cos不行呢?? [8.66025404e-01 5.00000000e-01 6.12323400e-17]
print(f'{np.sqrt(ndegree) = }')
print(f'{np.sin(ndegree) = }')

# degree to radians
print("180 / pi Degrees is equal to Radians : ", end ="")
print (math.radians(180 / math.pi))

ndrandom = np.random.randint(0,2,size=[2,4]) # 0~1隨機
print(f'{ndrandom = }')

# ----迭代 (記得攤平)---
import numpy as np
nditer001 = np.array([[1,2,3,4],[7,0,5,9]]) # 2x4
for row in nditer001:
    print(row)
for elem in nditer001.ravel(): # TODO #Python np.ravel() 可以有不同order的方式
    print(elem, end=" ")
for elem in nditer001.flat: #相同於ravel()扁平
    print(elem, end=" ")