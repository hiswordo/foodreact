
# ----生成式----
# @link [生成式 · Introducing python](https://iampennywu.gitbooks.io/introducing-python/content/chapter4-2.html) at 2021-08-11T10:11:25.
# * tuple 沒有生成式
# * Generator: Data to Iterator (產生器是一種將資料提供給迭代器的方式=重複性質)
# * 先有生成式，再決定數據類型，所以外框很重要，形成數據紀錄，直接print不會得到數據

# ----List Generator----
# 整數串列
# num_list = list(range(1,6))
# num_list = [num-1 for num in range(1,6)] # num-1 改變起始點
# print(num_list)

# 奇數串列
# num_list = [num for num in range(1,6,2)] # [1, 3, 5]
# num_list = [num for num in range(1,6) if num%2 == 1] # if 餘數2 表奇數 存入list
# print(num_list)

# tuple
# cells = [(row,col) for row in range(1,4) for col in range(1,3)]
# for cell in cells:
#     print(cell)

# rows = range(1,4)
# cols = range(1,3)
# cells = [(row,col) for row in range(1,4) for col in range(1,3)]
# for row, col in cells:  # tuple unpacking，從每一個 tuple 中拉出值
#     print(row, col)

# ----字典生成式----
# 計算Word的letter數
# word = 'yellowbanana'
# # letter_countlist = [word.count(letter) for letter in word]
# # print(letter_countlist.sort())
# letter_count = {letter: word.count(letter) for letter in word} # 同一個key，同value再跑一遍，只是更換字典內既有的項目
# print(letter_count)

# 如果要按abc排序
# word = 'yellowbanana'
# newWord = sorted(word)
# letter_count = {letter: word.count(letter) for letter in newWord}
# print(letter_count)

# word = 'yellowbanana'
# letter_countSet = {letter: word.count(letter) for letter in set(word)} # set()會重新排列，隨機放置letter
# print(set(word))
# print(letter_countSet)
# TODO #Python 這個字典的鍵的順序與之前的範例不同，因為迭代 set(word) 時，它回傳字母的順序與迭代 word 字串不同

# ----集合生成式----
# newSet = {element for element in range(1,6) if element%3 == 1}
# print(newSet)

# ! generator性質測試
# ? 另寫生成式再放到高階函式?? list set dict算嗎?
# number_thing = (number for number in range(1, 6))
# print(type(number_thing)) # <class 'generator'>

# print(number_thing) # <generator object <genexpr> at 0x0000000002106C80>
# print(hex(id(number_thing))) #0x2116c80

# print(list(number_thing)) # list、set皆可以，dic記得要{}大括號
# word = 'yellowbanana'
# number_thing = {letter: word.count(letter) for letter in word}
# print(dict(number_thing))

# ----五種底線----
# @link [Python - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/Python) at 2021-08-12T08:39:06.
# @link [Python Tricks — 底線家族的秘密. 在 Python 的世界裡，有一個神奇的符號 _ 底線… | by Gomax Lo | Python language | Medium](https://medium.com/python-language/python-tricks-%E5%BA%95%E7%B7%9A%E5%AE%B6%E6%97%8F%E7%9A%84%E7%A7%98%E5%AF%86-d84a2ce9cde6) at 2021-08-12T08:40:04.
# @link [Python中下劃線的5種含義 - 知乎](https://zhuanlan.zhihu.com/p/36173202) at 2021-08-12T08:40:12.
""" 
_spam（單底線開頭）：[文件獨有] 弱「內部使用」標識。對於from M import *，將不匯入所有以底線開頭的物件。
spam_（單底線結尾）：為了避免與python關鍵字的命名衝突。
__spam（雙底線開頭）：[Class獨有] 在命名一個類特性的時候，採用名字修飾，比如在類SpamEggs內，__spam將變成_SpamEggs__spam[68]。 # ! 避免SpamEggs有spam，RockEggs2也有spam，兩者不override，記得也是內部使用阿?
__spam__（雙底線開頭雙底線結尾）：[Python獨有] python獨有的「魔術」物件或特性，比如__name__、__doc__、__init__、__import__、__file__等。建議永遠不要將這樣的命名方式應用於自己的變數或函式。
_ (單底線) : 臨時變量、或稱不關心變數。ex: for _ in range(1,6)，跑六次迴圈，但不需要給予任何變數
 """

# ----海象運算符:=----
# @link [是时候将你的Python版本升级到3.8了！为什么我选择Python3.8？_你好，PurePeace！-CSDN博客](https://blog.csdn.net/qq_26373925/article/details/107674955) at 2021-08-12T11:33:04.
""" Python3.8
* 整體效能提升
* 新增海象運算符 := 與 f-string的=表達式
"""

# * 找1~4號，並找出不及格的 (2號已經退學)
# 原先打法
""" # 學生表（Key:value = id:{學生資料}）
students = {
    1: {'name': '小明', 'score': '及格'},
    3: {'name': '小红', 'score': '不及格'},
    4: {'name': '小绿', 'score': '不及格'}
}

results = []
for stuId in range(1, 5):
    student = students.get(stuId) # 如果是不存在的key则会取到None
    if student and student['score'] == '不及格': # 需要过滤掉是None的值，并取不及格的学生
        results.append(student)

print(results) """

# 海象打法
""" students = {
    1: {'name': '小明', 'score': '及格'},
    3: {'name': '小红', 'score': '不及格'},
    4: {'name': '小绿', 'score': '不及格'}
}

print([student := students.get(stuId) for stuId in range(1,5)])
print([student for stuId in range(1,5) if (student := students.get(stuId))!=None]) # if後面，海象要包起來()，才能執行
print([student for stuId in range(1,5) if (student := students.get(stuId))])  # 不等於None可省略
print([student for stuId in range(1,5) 
        if (student := students.get(stuId)) and student['score']=='不及格']) # 新增第二個條件
 """

# 任意數字直到想addup求和 (輸入addup以外會壞掉)
# 原先打法
""" inputs = []
while True:
    userInput = input('give me a number or"addup"：')
    if userInput == 'addup':
        break
    inputs.append(int(userInput))

print('求和的结果是：', sum(inputs)) """

# 海象打法
""" inputs = []
while (userInput:=input('give me a number or "addup"：')) != 'addup':
    inputs.append(int(userInput))
print('求和的结果是：', sum(inputs)) """

# ! 海象打法，少了括號 得到的結果[1,1,1,1]原因不明
""" inputs = []
while userInput:=input('give me a number or "addup"：') != 'addup':
    inputs.append(int(userInput))
print(inputs) # [1,1,1,1]
print('求和的结果是：', sum(inputs)) # 結果為4 """