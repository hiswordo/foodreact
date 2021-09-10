
# ----函式----
# @link [函式 · Introducing python](https://iampennywu.gitbooks.io/introducing-python/content/chapter4-4.html) at 2021-08-12T07:28:04.
# * 第一級公民: 可以將函式當成「串列、tuple、集合、字典元素」使用。
# ? 函式是不可變的，也可以將它們當成字典鍵
# ? 指派給變數、當成引數、在函式中回傳、很多Python獨有的特點

# ----函式當成資料在使用---- 
# * ()是呼叫函式!!「不使用括號」會「將函式視為其他的物件」

""" def run_something(func):
    func() # func傳入answer，執行answer()
def answer():
    print('OK')

run_something(answer) # !傳入的是 answer
print(type(answer)) # <class 'function'>
print(answer()) # !先執行answer()，再列印None，因為函數並沒有回傳任何值!
print(answer) # <function answer at 0x00000000023508B0> """

# *自我實踐
""" def run_op(func,*args):
    func(*args)

def add(*args):
    result = 0
    for arg in args:
        result += arg
    print(result)

def multi(*args):
    result = 1
    for arg in args:
        result *= arg
    print(result)

# 利用內建函數，sun原來可以傳入
def sum_args(*args):             # 定義函式 → 函式取用任意數量的位置引數 → 使用 sum() 函式來計算「引數總和」
    print(args)  # (3, 4, 2) tuple耶
    print(sum(args))

run_op(add,3,4,7,8) # 22
run_op(multi,3,4,2) # 24
run_op(sum_args,3,4,2) # 24 """

# ----內部函式----
# * 可以避免編寫重複的迴圈或程式碼
# * 外部執行的先看，執行內部函數並回傳

""" def outer(a, b):
    def inner(c, d): 
        return c + d
    return inner(a, b) # 執行inner，a,b會被c,d接收

print(outer(4, 7)) """

# 例子2
""" def knights(*saying):
    def inner(quote1,quote2):
        print(f"We are the knights who say: {quote1} and {quote2}")
    return inner(*saying)
knights('Ni!','No') """

# ----Closure----
# *wiki: a closure (also lexical closure or function closure) is a technique for implementing lexically scoped name binding in a language with first-class functions
# * 內部函式可以扮演 closure 的角色
# * 這是一種由「其他的函式動態」生成的函式，可以「更改或記得」函式之外的程式所建立的「變數的值」

""" def knights2(quote1):
    def inner2():  # 沒有引數直接用外面的
        print(f"We are the knights who say: {quote1}")
    return inner2 # 回傳函數名稱，不呼叫函數
a = knights2('Duck')
b = knights2('Hasenpfeffer')
# ! a、b 是函式，但它們也是 closure
print(type(a)) # <class 'function'>
print(a) # <function knights2.<locals>.inner2 at 0x0000000002380B80>
# 呼叫 a、b，它們會記得自己被 knights2 建立時「所使用的quote1」
a()
b() """
# 應該就是inner2()並會記得當初的quote1
# @link [聊聊 Python Closure. 今天來聊聊 Python 的 function closure。 | by Dboy Liao | Medium](https://dboyliao.medium.com/%E8%81%8A%E8%81%8A-python-closure-ebd63ff0146f) at 2021-08-12T09:24:35.

#----僅限位置形參---- 
# @link [是時候將你的Python版本升級到3.8了！ 為什麼我選擇Python3.8？ _你好，PurePeace！ -CSDN博客](https://blog.csdn.net/qq_26373925/article/details/107674955) at 2021-08-12T12:43:52.
# @link [Python 3.8 有什麼新變化 — Python 3.9.6 說明文件](https://docs.python.org/zh-tw/3/whatsnew/3.8.html) at 2021-08-12T12:44:12.
# / 之前只能給值，*之後只能給鍵與值，中間隨便
""" def newop(a,b,/,c,d,*,e,f):
    print(f'''[all parameter list]
        {a=}
        {b=}
        {c=}
        {d=}
        {e=}
        {f=}
    {a+b+c+d+e+f=}''')

newop(1,2,3,4,e=5,f=6)
newop(1,2,d=4,c=3,e=5,f=6) """

#----20210813_函式補充----
# @link 100days
# 在Python中，函式的引數可以有預設值(a=0)，也支援使用可變引數(*args)
# 所以，Python並不需要像其他語言一樣支援函式的過載
