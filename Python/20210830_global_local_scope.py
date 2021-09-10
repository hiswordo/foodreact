# https://www.w3schools.com/python/python_scope.asp

# global x = 10
x = 10
def myFunc():
    # 接下來的x宣告會作為global scope，那之前不能有區域宣告，不然就等於已經被區域宣告用了
    global x
    print(x)
    # global x = 5，不然本來def裡的宣告自動為區域宣告
    x = 5
    print(x)
myFunc()


