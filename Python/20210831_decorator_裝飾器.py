import time as t

# ----1 way----
""" def step1():
    start = t.time()
    b = 0
    for i in range(10000):
        b += 1
    print('this is step1')
    end = t.time()
    used = end - start
    print(f"{used=}")  # f"{used=}"顯示問題...好事真的是太快的問題，所以都等於0.0，還是因為run code的關係

step1() """

# ----2 way----
""" 
def step2():
    print('this is step2')

def timer(func):
    # 以下就是裝飾器
    def wrapper():
        start = t.time()
        func()
        end = t.time()
        used = end - start
        print(f"{used=}")
    return wrapper

time_step2fuc = timer(step2)
time_step2fuc()
# or 
timer(step2)() """

# %%
# ----3 way by decorator----
import time as t

def timer(func):
    # 以下就是裝飾器
    def wrapper():
        start = t.time()
        func()
        end = t.time()
        used = end - start
        print(f"{used}")
    return wrapper

# 告訴所以人要調用ste3()前得先經過timer()這一關
@timer
def step3():
    print('this is step3')

step3()

# ----Class中的裝飾器----
class Test(object):
    def _decorator(foo):
        def magic( self ) :
            print("start magic")
            foo( self )
            print("end magic")
        return magic

    @_decorator
    def bar( self ) :
        print("normal call")

test = Test()

test.bar()


# %%
# ----其他範例----
# @link [往函数上加多个装饰器怎么操作？python是如何装饰和执行它们的？ - YouTube](https://www.youtube.com/watch?v=U7Bu-Z0-TIY&loop=0) at 2021/8/31
# 購物密碼
""" def passwd(order):
    def checking():
        password = int(input("plz enter password:"))
        if password == 12345:
            order()
        else:
            print("wrong password")
    return checking

@passwd
def buy():
    print("Done of buying!")

# buy()
#如果上面沒有checking wrap起來的話，輸出的結果是會變AttributeError NoneType, None
print(buy.__name__, buy.__doc__) #checking, None
 """

# @link [快速理解並使用Python Decorator(裝飾器) | 只是個打字的](https://blog.typeart.cc/%E5%BF%AB%E9%80%9F%E7%90%86%E8%A7%A3%E4%B8%A6%E4%BD%BF%E7%94%A8Python%20Decorator/) at 2021/8/31
class decorateClass(object):
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"do something before calling function {self.func.__name__}")
        self.func(*args, **kwargs)
        print(f"do something after calling function {self.func.__name__}")

@decorateClass
def myFunc():
    print('主程式')

if __name__ == '__main__':
    myFunc()


