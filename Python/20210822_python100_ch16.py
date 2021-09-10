
# ----python100_ch16----
# ----enumerate
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# ----巢狀的列表的坑----
# *錄入五個學生三門課程的成績
names = ['關羽', '張飛']#, '趙雲', '馬超', '黃忠']
courses = ['語文', '數學','英語']
# scores = [[None] * len(courses)] * len(names)
#! []沒裝東西不能運算，所以[None]才可以
scores = [[None] * len(courses) for _ in range(len(names))]
print(scores)
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'請輸入{name}的{course}成績: '))
        print(scores)

# 挑戰字典{'關羽':{'語文':30,'數學':40},'張飛':{'語文':30,'數學':40}}

# ----生成式（推導式）的用法 字典----
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票價格大於100元的股票構造一個新的字典
print(prices.items())
prices2 = {key: value for key, value in prices.items() if value > 100}


# ----modules: 堆積佇列(heap queue)----
"""
從列表中找出最大的或最小的N個元素
堆結構(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

