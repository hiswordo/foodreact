# @link [Python 面試複習題整理 |Python 主題月 - 掘金](https://juejin.cn/post/6990156706164506655) at 2021/9/3
# ---- ----
# @link [Python中的id函式到底是什麼？ - IT閱讀](https://www.itread01.com/content/1549999452.html) at 2021/9/3
# @link [Python编程学习5：python id()函数和内存分配理解_zhuzuwei的博客-CSDN博客](https://blog.csdn.net/zhuzuwei/article/details/80554776) at 2021/9/3
""" 
>可更改（mutable）與不可更改（immutable）物件：
不可變類型：變數賦值 a=5 后再賦值 a=10，這裡實際是新生成一個 int 值物件 10，再讓 a 指向10，而 5 被丟棄，不是改變a的值，相當於新生成了a。
可變類型：變數賦值 la=[1，2，3，4] 后再賦值 la[2]=5 則是將 list la 的第三個元素值更改，本身la沒有動，只是其內部的一部分值被修改了。
immutable objects:
    Numeric types: int, float, complex
    string
    tuple
mutable objects:
    list
    dict
    set
"""
# 測試結果:
# id代表其唯一不變身分證，泛指mutable obj=list之類的，但要注意普通變數是會隨值而變的，包含list[2]，因為id是跟隨著數字跟字串
# 只要是實際存儲一個值的，都是用指向的，都是不可變類型immutable 
# 每次執行程式碼，id皆會同

# 同py檔內，相同數字/字串，皆為同一id，那些指向他的變數亦同 (但2與2.0並不相同)
a = 1
b = 1
print(f"{id(a)=}, {id(b)=}, {id(1)=}")
print(id(a) == id(b) & id(a) == id(1))  # True

# 就算直接id(未指定數字)亦可作用，其後的變數仍指向同id
# *新申請一段記憶體來存儲物件0，再讓c去指向物件0
print(id(0))  # 常數、字串等可以直接id，變數不行
c = 0
print(id(c) == id(0))  # True

# List的id狀況，List不變，但裡面的不同位置可以指向不同的記憶體可變
rock = [1, 2, 3]
print(id(rock))
print(id(rock[0]), f"\n{id(rock[2])=}\n", id(rock[2]))
rock[2] = 5
print(f"{id(rock[2])=}")
# 8790473311920 id(rock[2])=8790473311984 8790473311984
# id(rock[2])=8790473312048


# 數值很大的int物件，python才會分別申請一塊記憶體，來存儲
e = 33**50 
f = 33**50 
print(id(33**50)) # 6942256
print(id(e)) # 6942448
print(id(f)) # 6942512
print(e == f) # True
print(e is f) # False




""" 
>補充:
1、id(object)返回的是物件的“身份證號”，唯一且不變，但在不重合的生命週期裡，可能會出現相同的id值。此處所說的物件應該特指複合型別的物件(如類、list等)，對於字串、整數等型別，變數的id是隨值的改變而改變的。
2、一個物件的id值在CPython直譯器裡就代表它在記憶體中的地址。(CPython直譯器：http://zh.wikipedia.org/wiki/CPython) 
"""


lis = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lis[:5:-2])
