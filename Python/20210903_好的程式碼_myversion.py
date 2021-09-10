"""
解決五問題:
Error: 可避免錯誤 (Edge Case的測試)
Repeat: 重複程式碼少 
Mixed: 各種動作分開 (可讀性也會提高，可擴展性也高)
Unreadable: 確認是否能一眼就懂 (註解夠精簡，程式碼夠好懂)
Weak: 分配各種動作歸屬 (建立類型、物件、變數的藍圖) # ?? 這要靠甚麼方式呢?
總結: 「容錯」、「精簡」、「可擴充」、「易讀」、「再利用」
"""
# ! 發現寫複雜的程式，先用代名詞沒關係，之後在整體改名就好了??
# class後，真的方便許多，也可讀許多! 應該說它會讓我注意到原本那些東西會重複，那些東西的命名是沒用的
# 原則上，假設原本輸入的數值，做了很多手續，但都只是調整數列狀態的話，寫成一列屬性，很方便! 需要直接取用即可
# !所以循環式的方式，寫出來的程式也就直接不太會重複了
# 最大公因數and最小公倍數，甚至可以列出因式分解，所有因數排列組合等


def primeFactorize(num):
    denumerator = 2
    primeFactorization = dict()
    # 從最小數字開始除，同質數也要重複除
    while denumerator <= num:  # ?? num > 1 會不會有差呢?
        if num % denumerator == 0:
            # ?? 不懂為什麼不能 i += 1 的寫法
            primeFactorization[denumerator] = primeFactorization.get(denumerator, 0) + 1
            num /= denumerator
        else:
            denumerator += 1
    return primeFactorization


def findGCF(*nums):
    numDictList = [primeFactorize(num) for num in nums]
    primeDictList = [set(num.keys()) for num in numDictList]

    # *累交集，需先定義交集為第一個集合，不然因為沒交集直接就變空集合了set()
    commonPrime = set(numDictList[0].keys())
    for prime in primeDictList[1:]:
        commonPrime &= prime

    # 尋找每個同質數裡，次方最小的，並加入
    gcf = 1
    for prime in commonPrime:
        i = 0
        minPower = 1
        for i in range(len(numDictList)):
            minPower = min(minPower, numDictList[i][prime])
        gcf = gcf * (prime ** minPower)
    return gcf


print(findGCF(30, 45, 60))

from functools import reduce


class Calc:
    def __init__(self, *nums):
        self.nums = [num for num in nums]
        self.priFactorization = [self.__primeFactorize(num) for num in nums]
        self.priFactors = [set(num.keys()) for num in self.priFactorization]
        self.intersectFactors = reduce(lambda x, y: x & y, self.priFactors)
        self.uninonFactors = reduce(lambda x, y: x | y, self.priFactors)
        self.mylist = self.prlist()
        self.allFactors = self.__findFactors()

    def __primeFactorize(self, num):
        denumerator = 2
        primeFactorization = dict()
        # 從最小數字開始除，同質數也要重複除
        while denumerator <= num:  # ?? num > 1 會不會有差呢?
            if num % denumerator == 0:
                primeFactorization[denumerator] = (
                    primeFactorization.get(denumerator, 0) + 1
                )
                num /= denumerator
            else:
                denumerator += 1
        return primeFactorization

    def __findFactors(self):
        """ 
        allFactors = []
        for num in self.nums:
            factors = []
            for factor in range(1, num + 1):
                if num % factor == 0:
                    factors.append(factor)
                else:
                    continue
            allFactors.append(factors)  # 反正每一個數的因數一定從第一位開始append阿，不需要設定位置
        return allFactors
        """
        # 方法二，將每組數據依序乘上去，並由小到大排列，並加到list上
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
        return ultiResult
    
    # 排列所有質因數*所有次方
    def prlist(self):
        mylist = []
        for i in range(len(self.priFactorization)):
            a = list(self.priFactorization[i].keys())
            b = self.priFactorization[i]
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
        return mylist

    # 兩list互相相乘
    def multiplylist(self, xs, ys=1):
        newlist = []
        for x in xs:
            for y in ys:
                newlist.append(x*y)
        return newlist

    def findGCF(self):
        gcf = 1
        for prime in self.intersectFactors:
            i = 0
            minPower = 1
            for i in range(len(self.priFactorization)):
                minPower = min(minPower, self.priFactorization[i][prime])
            gcf = gcf * (prime ** minPower)
        return gcf

    def findLCM(self):
        lcm = 1
        for prime in self.uninonFactors:
            i = 0
            minPower = 1
            for i in range(len(self.priFactorization)):
                minPower = max(minPower, self.priFactorization[i].get(prime, 0))
            lcm = lcm * (prime ** minPower)
        return lcm

    # TODO 排列組合來算所有因數的話有點難寫喔
"""     def listAllFactors(self, item):
        listFactors = []
        for key in [self.factorization[item-1].keys()]:
            for pow in range(0,self.factorization[key]):
                key ** pow """

nw = Calc(30, 40)
print(f"{nw.nums=}")
print(f"{nw.priFactorization=}")
print(f"{nw.priFactors=}")
print(f"{nw.intersectFactors=}")
print(f"{nw.uninonFactors=}")
print(f"{nw.allFactors=}")

print(nw.findGCF())
print(nw.findLCM())

print(nw.mylist)
