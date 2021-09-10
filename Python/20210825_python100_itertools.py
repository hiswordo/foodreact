# ----modules: 迭代工具模組(itertools、more-itertools )----
"""
迭代工具模組
- 能夠方便地處理 iterable （例如 dict, list, tuple, str 等類型的資料），譬如環型走訪、分類群組(group by)、乘積(product）
- 還可以安裝 pip install more-itertools
# @link [itertools --- 为高效循环而创建迭代器的函数 — Python 3.9.6 文档](https://docs.python.org/zh-cn/3/library/itertools.html) at 2021/8/25
# @link [More Itertools — more-itertools 8.8.0 documentation](https://more-itertools.readthedocs.io/en/stable/index.html) at 2021/8/25
"""
# @link [Python 好用模組介紹 - itertools & more-itertools](read://https_myapollo.com.tw/?url=https%3A%2F%2Fmyapollo.com.tw%2Fzh-tw%2Fpython-itertools-more-itertools%2F) at 2021/8/25
# ----list內走訪7步----
# 傳統作法
countTime = 7
count = 1
cyclelist = ["A", "B", "C", "D"]
while count > 0:
    for x in cyclelist:
        print(count, ": ", x)
        if count == countTime:
            count = -1
            break
        count += 1

# *itertools.cycle 無窮迭代(無限迴圈序列)
from itertools import cycle
count = 1
cyclelist = ["A", "B", "C", "D"]
for x in cycle(cyclelist):
    print(count, ": ", x)
    if count == 7:
        break
    count += 1

# more-itertools 的 ncycles，如果整數倍循環最簡潔
# list循環兩次
from more_itertools import ncycles
cyclelist = ["A", "B", "C", "D"]
idx = 0
for x in ncycles(cyclelist, 2):
    idx += 1
    print(f"{idx}: {x}")

# ----排列组合----
# 排列 產生ABCDE的4選2排列
from itertools import permutations
print(list(permutations("ABCD", 2)))
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]

# 組合 產生ABCDE的4選2組合
from itertools import combinations
print(list(combinations('ABCD', 2)))
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

# 產生ABCD和123的笛卡爾積
from itertools import product
# print(list(product('ABCD', '123')))

# 99乘法表
""" for x in range(1, 10):
    for y in range(1, 10):
        print(f'{x} x {y} = {x*y}') """

# 一行解決99乘法表
""" for x, y in product(range(1, 10), range(1, 10)):
    print(f'{x} x {y} = {x*y}') """

# 還可以處理多層迴圈
""" for x, y, z in product(range(1, 3), range(1, 4), range(1, 5)):
    # print(f'{x} x {y} x {z} = {x*y*z}')
    print(f'{x} + {y} x {z} = {x+y*z}')
 """
