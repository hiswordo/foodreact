""" from functools import reduce
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5]) 
print(sum2) """

""" for x in range(1,4):
    print(x)

lislist = [7,3,5,9]
print(list(enumerate(lislist))[0][0]) """

# [[[1, 2], [1, 3], [1, 5]], [[1, 2, 4, 8], [1, 5]]]
# [[1, 2, 3, 5, 6, 10, 15, 30], [1, 2, 4, 5, 8, 10, 20, 40]]
""" def __findFactors(self):
    ultiResult = []
    outresult = []
    for j in range(len(self.mylist)):
        if len(self.mylist[j]) == 1:
            outresult.append(self.mylist[j])
        else:
            result = self.mylist[j][0]
            for i in range(1,len(self.mylist[j])):
                result = self.multiplylist(result, self.mylist[j][i])
            outresult = result
        ultiResult.append(sorted(outresult))
    return ultiResult """

# [{2: 1, 3: 1, 5: 1}, {2: 3, 5: 1}]
# [[[1, 2], [1, 3], [1, 5]], [[1, 2, 4, 8], [1, 5]]]
# 建立num的質因數所有次方的清單

""" original = [{2: 1, 3: 1, 5: 1}, {2: 3, 5: 1}]

def prlist():
    
    mylist = []
    for i in range(len(original)):
        a = list(original[i].keys())
        b = original[i]
        outterlist = []
        for x in a:
            pow = 0 
            innerlist = []
            for pow in range(b[x]+1):
                innerlist.append(x**pow)
                # print(f"{innerlist=}")
            outterlist.append(innerlist)
            # print(f"{outterlist=}")
        mylist.append(outterlist)
    return mylist """

# %%
import pandas as pd

selected_year = 2001
# def load_data(year):
url = (
    "https://www.basketball-reference.com/leagues/NBA_"
    + str(selected_year)
    + "_per_game.html"
)
html = pd.read_html(url, header=0)  # <class 'list'>
df = html[0]  # <class 'pandas.core.frame.DataFrame'>
# df.Tm.unique()
df.corr()
# raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
# raw = raw.fillna(0)
# playerstats = raw.drop(['Rk'], axis=1)
# df.iloc[21:27]
# return playerstats
# playerstats = load_data(selected_year)
# playerstats

# %%
# 函數中的函數
def callother(func):
    return func()


def add():
    print("add")


callother(add)
# %%
def run_op(func, *args):
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
def sum_args(*args):  # 定義函式 → 函式取用任意數量的位置引數 → 使用 sum() 函式來計算「引數總和」
    print(args)  # (3, 4, 2) tuple耶
    print(sum(args))


run_op(add, 3, 4, 7, 8)  # 22
run_op(multi, 3, 4, 2)  # 24
run_op(sum_args, 3, 4, 2)  # 24

# %%

# Case A in B without Case Sensitive
def rAinB(a, b):
    return a.lower() in b.lower()

print(rAinB("no","Saying Nothing"))



# %%
