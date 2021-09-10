
# @link [Python Tutorial: Generators - How to use them and the benefits you receive - YouTube](https://www.youtube.com/watch?v=bD05uGo_sVI&loop=0) at 2021/9/1
# @link [Python反覆運算和解析（5）：搞懂生成器和yield機制 - 駿馬金龍 - 博客園](https://www.cnblogs.com/f-ck-need-u/p/10266226.html) at 2021/9/1
""" 
使用 mem_profile 跟 time 可以測出
list 1000000 筆資料，大約佔內存 318-15mb = 300mb左右，時間花費 1.2s
但使用yield 或 generator 完全不佔內存，時間花費才 2e-06s
"""
""" 
記憶: 生成式的前身
結果: 用yield，逐次回傳結果，使用迴圈組成generator
好處: 可讀性變高，節省內存資源
特性: 
1. 只需佔用一個元素的記憶體空間
2. for迴圈碰到yield結束迴圈
3. 返回值於每次反覆運算才逐次由next恢復掛起的yield (分散使用資源的概念)
4. 不同於return，不會退出函數，直到使用完畢!
P.S. 反覆運算器用於從數據集中取出元素; 而生成器用於"憑空"生成（yield）元素
"""
# ----傳統list:佔資源----
def square_number(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_number([1, 2, 3, 4, 5])

print(my_nums)  # [1, 4, 9, 16, 25]


# ----yield----
def square_numbery(nums):
    for i in nums:
        yield i * i

# 呼叫產生器函數的時候並沒有執行函數體中的代碼，它僅僅只是返回一個產生器物件。
my_nums = square_numbery([1, 2, 3, 4, 5])  

print(my_nums)  # <generator object square_numbery at 0x0000000001D63EB0>
print(next(my_nums)) # 1
print(next(my_nums)) # 4
print(list(my_nums)) # [9, 16, 25]
my_nums.send(2)
print(next(my_nums)) # StopIteration

# 也可以用迴圈來取用
for i in my_nums:
    print(i)


# ----generator----

my_nums = (x*x for x in [1,2,3,4,5]) # <generator object <genexpr> at 0x0000000001D33EB0>
print(my_nums)

my_nums = [x*x for x in [1,2,3,4,5]] # [1, 4, 9, 16, 25]
print(my_nums)


#----進階yield----
# ?? 有點累
def mygen():
  x = yield 111         # (1)
  print("x:", x)        # (2)
  for i in range(5):    # (3)
    y = yield i         # (4)
    print("y:", y)      # (5)

M = mygen()
print("first:",next(M)) # first: 111 # 如果再next一次則會得到 X : None，first: 0
print("second:",M.send(10)) # x: 10
print("third:",M.send(11))

yield 10            # (1) 丢弃yield的返回值
x = yield 10        # (2) 将yield返回值赋值给x
x = (yield 10)      # (3) 等价于 (2)
x = (yield 10) + 11 # (4) 将yield返回值加上11后赋值给x

# 上面的4種yield表達式方式中，如果使用next（）來恢復yield
yield 10       # 先产生10发送出去，然后返回None，但丢弃
x = yield 10   # 返回None，赋值给x
x = (yield 10) # 与上等价
x = (yield 10)+11 # 返回None，整个过程报错，因为None和int不能相加

# 其實next（）可以看作是等價於。gen.send(XXX) XXX gen.send(None)
# yield表達式會在產生一個值后立即掛起，它連返回值都是在下一次才返回的。