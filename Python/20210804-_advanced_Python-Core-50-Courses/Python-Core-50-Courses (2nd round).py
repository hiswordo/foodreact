#https://github.com/jackfrued/Python-Core-50-Courses
"""saved
撲克遊戲
52張牌發給四個人:按黑桃、紅心、草花、方塊的順序和點數從小到大排列
"""
import random

cardSuite = ['♠','♥','♣','♦'] #['spade','heart','club','diamond'] ord:9824 9829 9827 9830

# 建立撲克牌的定義
class Card:
    def __init__(self,suite,num):
        self.suite = suite
        self.num = num
    def __repr__(self) -> str:
        return f'{self.suite}{self.num}'
    # def __lt__(self, other): # 魔法less than [♠1, ♠3, ♠8, ♣3, ♣8, ♣12, ♥2, ♥4, ♥8, ♥12, ♦1, ♦4, ♦6] 好強!
    #     if self.suite == other.suite: #顏色相同比數字
    #         return self.num < other.num
    #     return self.suite < other.suite #顏色不同，比顏色
    def __lt__(self, other): # 
        if self.suite == other.suite: 
            return self.num < other.num
        return cardSuite.index(self.suite) < cardSuite.index(other.suite) 
        #按照['♠','♥','♣','♦']排列 [♠8, ♠10, ♠12, ♥7, ♣3, ♣5, ♣8, ♦1, ♦2, ♦6, ♦9, ♦10, ♦11]

# 建立新的一副撲克牌
carddeck = []
for i in cardSuite:
    for j in range(1,14):
        carddeck.append(Card(i,j))

# 洗牌+發牌
random.shuffle(carddeck)
player01 = carddeck[0:13]
player02 = carddeck[13:26]
player03 = carddeck[26:39]
player04 = carddeck[39:52]
print(type(player01))  # <class 'list'>
print(player01) #[♥7, ♥12, ♠2, ♣1, ♣11, ♥4, ♣2, ♦6, ♦13, ♥3, ♥8, ♥6, ♥13]
print(type(player01[1])) # <class '__main__.Card'>
# 用物件指向的__lt__搭配sort理牌
player01 = sorted(player01)
# 用轉str的方式搭配sort理牌
# player01[:] = [str(x) for x in player01] # list列表轉型態生成式! => ['♥7', '♥12'...]
# 上列等同:player01 = list(map(str,player01))  # map針對list元素做同動作處理 #!map返還值是iterators
# player01 = sorted(player01) # '♠','♣','♥','♦' ['♠11', '♠2', '♠5', '♠6', '♠9', '♣13', '♣9', '♥12', '♥3', '♥5', '♥8', '♦12', '♦7']
print(player01)

# *2021-08-08 第020課：函式使用進階

# https://www.gushiciku.cn/pl/gYqb/zh-tw

# 關鍵字引數 (限定用法)
# 加上*，傳參時必須使用“引數名=引數值”的方式，位置不重要
# def can_form_triangle(*, a, b, c):
#     print(type(a))
#     print(f'a = {a}, b = {b}, c = {c}')
#     return a + b > c and b + c > a and a + c > b
# print(can_form_triangle(a=3, b=4, c=5))
# print(can_form_triangle(c=5, b=4, a=3))

# 可變長度_關鍵字引數 = var-keyword parameter
# def fn(**a):
#     for i in a.items(): # items() = (key(), values())
#         print(a) # dict
#         print(i) # tuple
# fn(numbers=5,colors="blue",fruits="apple")

# 可變長度_位置引數=可變引數 = var-positional parameter # 改建中
# def calc(*args):
#     result = 0
#     ops = ['+','-','*','/']
#     for arg in args:
#         result = result + arg
#     return result
# print(calc(1,2,23))

# 合併使用 #!實在有夠難想哪裡用
# def calc(*args, **kwargs):  # (tuple, dict)
#     result = 0
#     for arg in args:
#         result += arg
#         print('this is',type(args))
#     for value in kwargs.values():
#         result += value
#         print(type(kwargs))
#     return result

# print(calc())                  # 0
# print(calc(1, 2, 3))           # 6
# print(calc(a=1, b=2, c=3))     # 6
# print(calc(1, 2, c=3, d=4))    # 10

# 高階函數
""" def is_even(num):
    return num % 2 == 0
def square(num):
    return num ** 2
numbers1 = [35, 12, 8, 99, 60, 52]
bridge1 = filter(is_even, numbers1) #<filter object at 0x00000000023762E0>
numbers2 = list(map(square, bridge1)) # map(square, bridge1) <map object at 0x0000000002396CD0>
print(bridge1, numbers2, end='\t') """

# Lambda
# def calc(*args, init_value=0, op=lambda x, y: x + y):
#     result = init_value
#     for arg in args:
#         result = op(result, arg)  # result = op(result, arg) = op(x,y) if = x + y = result + arg
#     return result
# print(calc(2,3,4,5, init_value=1, op=lambda x, y: (x * y * 2))) 

# *2021-08-08 第006課：迴圈結構
# for-in
# print(range(1))  # range(0, 1)
# list = ['a','b','c']
# x = 0
# for i in range(2): # a b
#     x += 1
#     print(list[i])
# print(x)

# x = 0
# for i in range(1, 101):
#     x += 1
# print(x)

# x = 0
# for i in range(1, 101, 1):
#     x += 1
# print(x)

# *2021-08-08 第008課：函式和模組
# def add(a):
#     result = a+3
# print(add(3)) # 沒有return值，add()為None

# def add(a=0, b=0, c=0):
#     return c - a + b
# print(add()) # 沒有引數，有預設，add()為0-0+0
# print(add(1)) # 0-1+0
# print(add(1,2,3)) # 3-1+2
# print(add(c=3,b=2,a=1)) # 3-1+2 如果引數不按照順序，但要標記

# def add(a, b=0, c=0): #不帶預設值的引數排前面
#     return a+b+c
# print(add(1))

# *2021-08-08 第009課：常用資料結構之字串
# print(ord('a'))
# print(chr(65))
# x=123
# y=3.145
# print(f'{x:x<10d}gogo{y:+.2f}') # x

# *2021-08-08 第011課：常用資料結構之列表
# items = ['Python', 'Java', 'Go', 'Kotlin']
# items.pop(0) #斬頭
# items.pop(len(items) - 1) #去尾
# print(items)    # ['SQL', 'Go']

# items = ['Python', 'Java', 'Go', 'Kotlin']
# element = items.pop(0)  # @learn pop有返回值
# print(element)

# 列表生成式
# L = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"
# N = L.split(",")
# print([int(N[i]) for i in range(0,14,3)])
# # 建立一個由1到9的數字構成的列表
# items1 = [x for x in range(1,10)]
# # 建立一個由'hello world'中除空格和母音字母外的字元構成的列表
# items2 = [x for x in 'hello world' if x not in ' aeiou']
# # 建立一個由個兩個字串中字元的笛卡爾積構成的列表
# items3 = [x+y for x in 'ABC' for y in '12']
# print(items1,items2,items3,sep='\n')

# *2021-08-08 第012課：常用資料結構之元組
# a, b, *c = range(1, 10)
# print(a, b, c)
# a, b, c = [1, 10, 100]
# print(a, b, c)
# a, *b, c = 'hello'
# print(a, b, c)


"""
將一顆色子擲6000次，統計每個點數出現的次數。
"""
# import random
# counter=[0]*6
# for _ in range(6000):
#     face = random.randint(1,6)
#     counter[face-1] += 1
# for face in range(1,7):
#     print(f'{face}點總共出現了{counter[face-1]}次')

"""
獲取檔名的字尾名
:param filename: 檔名
:return: 檔案的字尾名
"""
# def get_suffix(filename):
#     pos = filename.rfind('.')
#     # 通過切片操作從檔名中取出字尾名
#     return filename[pos+1:] if pos > 0 else '' #!啥鬼語法 print('thx') if x>0 else print('x is negative')

# # from os.path import splitext
# # def get_suffix(filename):
# #     return splitext(filename)[1][1:]

# print(get_suffix('readmetxt'))       # txt
# print(get_suffix('readme.txt.md'))    # md

'''
指定長度驗證碼的函式 (10組隨機驗證碼，長度4)
'''
# import random
# ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# def generate_code(code_len=4):
#     code=''
#     for _ in range(code_len): #每一圈抓一個字母，預設抓四次
#         index = random.randrange(0,len(ALL_CHARS))
#         code += ALL_CHARS[index]
#     return code
# for _ in range(3): #抓三組
#     print(generate_code(6))

# 方法2
# import random
# import string
# ALL_CHARS = string.digits + string.ascii_letters # 數字+英文(不分大小寫)
# def generate_code(code_len=4):
#     return ''.join(random.choices(ALL_CHARS, k=code_len)) # k=多少，取幾位['V', 'D', 'M', 'F'...]，然後再字串函式join合併起來
# print(generate_code())

"""
可變引數: 任意多個數求積
"""
# def times(*multip):
#     total = 1
#     # 可變引數可以放在for迴圈中取出每個引數的值
#     for val in multip:
#         total *= val
#     return total
# print(times(2,3,4)) # 2x3x4

"""
將華氏溫度轉換為攝氏溫度
"""
# f = float(input('請輸入華氏溫度: '))
# c = (f - 32) / 1.8
# print(f'{f:}華氏度 = {c:.1}攝氏度') #小數點下幾位:.1，一位，.2，兩位 (會四捨五入)
# c = (f - 32) / 1.8
# t = 70
# # print('%.1f華氏度 = %.1f攝氏度%d' %(f, c, t))

"""
列印乘法口訣表
"""
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i}x{j}={i*j}',end='\t')
#     print()

# for i in range(1, 10):
#     for j in range(1, i+1): #數到自己，例如5x5，不要5x6
#         print(f'{i}*{j}={i*j}', end='\t') # 結尾默認為end='\n'，\t表tab製表符
#     print() # \n

"""
輸入一個正整數判斷它是不是素數
# """
# num = int(input('我幫你判斷是否為質數，給我一個數?'))
# for i in range(2,num): # 頭尾都不取，1跟自己本身以外都不能整除
#     unum_ck = num % i
#     if unum_ck == 0:
#         is_jnum = False
#         print(f'{num}不是質數')
#         break
#     else:
#         is_jnum = True
# if is_jnum:
#    print(f'{num}是質數')


# is_unum = False
# print(is_unum)
# if not is_unum:
# num = 7%3
# print(num)

"""
輸入兩個正整數計算它們的最大公因數和最小公倍數
"""
# 想法:公因數兩數取較小，從較小逆著越來越小，依序除以兩數。公倍數取最大，從最大開始乘上，越來越大
# def divinum2(numi1,numi2):
#     if numi1 >= numi2:
#         num1 = numi1
#         num2 = numi2
#     else:
#         num1 = numi2
#         num2 = numi1
#     for i in range(num2,0,-1):
#         if num2%i == 0:
#             # print(f'小數的因數有{i}')
#             num1_ck = num1%i == 0
#             num2_ck = num2%i == 0  
#             if num1_ck and num2_ck:
#                 print(f'最大公因數為{i}')
#                 break

# print('求兩數的最大公因數')
# num1 = int(input('先給我一個數:'))
# num2 = int(input('再給我一個數:'))
# divinum2(num1,num2)


# 公倍數 = 大數x小數的因數
# def timesnum2(numi1,numi2):
#     if numi1 >= numi2:
#         num1 = numi1
#         num2 = numi2
#     else:
#         num1 = numi2
#         num2 = numi1
#     for i in range(1,num1*num2+1):
#         if num2%i == 0:
#             # print(f'小數的因數有{i}')
#             num1_ck = (i*num1)%num1 == 0
#             num2_ck = (i*num1)%num2 == 0
#             if num1_ck and num2_ck:
#                 print(f'最小公倍數為{i*num1}')
#                 break

# print('求兩數的最小公倍數')
# num1 = int(input('先給我一個數:'))
# num2 = int(input('再給我一個數:'))
# timesnum2(num1,num2)

"""
找出所有水仙花數
"""
# 三位數表達:1.三層迴圈 2.除以100，10的餘數 3.str與int互轉。用3.看看
# for i in range(100,1000):
#     strlist = list(str(i)) # 三位數轉字串，再拆成list
#     hunnum, tennum, num = int(strlist[0]), int(strlist[1]), int(strlist[2]) # list各自轉回百位，十位，個位數字
#     formalTotal = hunnum**3 + tennum**3 + num**3
#     if formalTotal == i:
#         print(i,end='\t')

"""
輸入M和N計算C(M,N) # permutation and combination
"""
# M!/(M-N)!N!
# def combina(M,N):
#     if M > N:
#         mTotal = M
#         nTotal = N
#         mnTotal = M-N
#         for i in range(M-1,0,-1):
#             mTotal = mTotal*i
#         for j in range(N-1,0,-1):
#             nTotal = nTotal*j
#         for k in range(M-N-1,0,-1):
#             mnTotal = mnTotal*k
#         result = mTotal//(nTotal*mnTotal) # 利用//強制去掉.0
#         return result
#     elif M == N:
#         result = 1
#         return result
#     else:
#         return '值可能填反了喔!這樣無法取Combination呢'

# print(combina(3,7)) # 35

"""
輸入M和N計算C(M,N) # permutation and combination
"""
# m = int(input('m = '))
# n = int(input('n = '))
# def fac(num): # 求階乘factorial
#     result = 1
#     for num in range(1, num+1):
#         result *= num
#     return result
# print(fac(m)//fac(n)//fac(m-n))

