# https://www.w3schools.com/python/python_scope.asp
# global x = 10
x = 10
def myFunc():
    # 接下來的x宣告會作為global scope，那之前不能有區域宣告，不然就等於已經被用了
    global x
    print(x)
    # global x = 5
    x = 5
    print(x)
myFunc()

