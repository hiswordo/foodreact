# @link [物件導向武功秘笈（1）：認知篇 — 什麼是好的程式？ - YC Note](https://www.ycc.idv.tw/introduction-object-oriented-programming_1.html) at 2021/9/3
"""
解決五問題:
Error: 可避免錯誤 (Edge Case的測試)
Repeat: 重複程式碼少 
Mixed: 各種動作分開 (可讀性也會提高，可擴展性也高)
Unreadable: 確認是否能一眼就懂 (註解夠精簡，程式碼夠好懂)
Weak: 分配各種動作歸屬 (建立類型、物件、變數的藍圖) # ?? 這要靠甚麼方式呢?
總結: 「容錯」、「精簡」、「可擴充」、「易讀」、「再利用」
"""
""" 
大原則:「正常執行」、「不重複撰寫」、「穩健」、「可擴展」、「強化」、「可讀性」
「穩健」、「可擴展」單元: 低耦合(low Coupling)、高內聚(high Cohesion)
    耦合性:「單元」和「單元」之間資訊或參數依賴的程度
    聚合性:「單元」內使用到自身資訊或參數的程度
    兩者相依 
"""

# 例子: 求最大公因數的計算機


def main():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")

    numA = int(str_numA)
    numB = int(str_numB)

    # 因式分解
    prime_factorize_A = dict()
    i = 2
    while numA > 1:
        if numA % i == 0:
            prime_factorize_A[i] = prime_factorize_A.get(i, 0) + 1
            numA /= i
        else:
            i += 1

    prime_factorize_B = dict()
    i = 2
    while numB > 1:
        if numB % i == 0:
            prime_factorize_B[i] = prime_factorize_B.get(i, 0) + 1
            numB /= i
        else:
            i += 1

    # 取出共同公因數
    common_prime = set(prime_factorize_A.keys()) & set(prime_factorize_B.keys())

    # 取出公因數的次方(較小的即是ex 2^5=2^3*2^2)
    gcf = 1
    for prime in list(common_prime):
        m = min(prime_factorize_A[prime], prime_factorize_B[prime])
        gcf = gcf * (prime ** m)

    print("Greatest Common Factor: " + str(gcf))


# ---- 1.「正常執行」Error ----

# 很明顯，輸入0或負號即會報錯
def mainE():
    str_numA = input("Positive Integer A: ")
    numA = int(str_numA)
    if numA <= 0:
        raise ValueError("invalid positive integer: " + str(numA))

    str_numB = input("Positive Integer B: ")
    numB = int(str_numB)
    if numB <= 0:
        raise ValueError("invalid positive integer: " + str(numB))

    # 因式分解
    prime_factorize_A = dict()
    i = 2
    while numA > 1:
        if numA % i == 0:
            prime_factorize_A[i] = prime_factorize_A.get(i, 0) + 1
            numA /= i
        else:
            i += 1

    prime_factorize_B = dict()
    i = 2
    while numB > 1:
        if numB % i == 0:
            prime_factorize_B[i] = prime_factorize_B.get(i, 0) + 1
            numB /= i
        else:
            i += 1

    # 取出共同公因數
    common_prime = set(prime_factorize_A.keys()) & set(prime_factorize_B.keys())

    # 取出公因數的次方(較小的即是ex 2^5=2^3*2^2)
    gcf = 1
    for prime in list(common_prime):
        m = min(prime_factorize_A[prime], prime_factorize_B[prime])
        gcf = gcf * (prime ** m)

    print("Greatest Common Factor: " + str(gcf))


# ---- 1.「不重複撰寫」Repeat ----


def checkPositiveInteger(num):
    if (not isinstance(num, int)) or (num <= 0):
        raise ValueError("invalid positive integer: " + str(num))


def primeFactorize(num):
    checkPositiveInteger(num)

    prime_factorize = dict()
    i = 2
    while num > 1:
        if num % i == 0:
            prime_factorize[i] = prime_factorize.get(i, 0) + 1
            num /= i
        else:
            i += 1
    return prime_factorize


def mainER():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")

    numA = int(str_numA)
    numB = int(str_numB)

    prime_factorize_A = primeFactorize(numA)
    prime_factorize_B = primeFactorize(numB)

    common_prime = set(prime_factorize_A.keys()) & set(prime_factorize_B.keys())

    gcf = 1
    for prime in list(common_prime):
        m = min(prime_factorize_A[prime], prime_factorize_B[prime])
        gcf = gcf * (prime ** m)

    print("Greatest Common Factor: " + str(gcf))

# ---- 3.「穩健度」和「可擴展」Mixed----
# 問題: 客戶端邏輯和業務邏輯混為一談
""" import sys
def checkPositiveInteger(num):
    if (not isinstance(num,int)) or (num<=0):
        raise ValueError("invalid positive integer: "+str(num))

def primeFactorize(num):
    checkPositiveInteger(num)

    prime_factorize = dict()
    i = 2
    while(num > 1):
        if num % i == 0:
            prime_factorize[i] = prime_factorize.get(i,0) + 1
            num /= i
        else:
            i += 1
    return prime_factorize

def findGCF(nums):
    prime_factorize = list()
    for num in nums:
        prime_factorize.append(primeFactorize(num))

    common_prime = set(prime_factorize[0].keys())
    for pf in prime_factorize[1:]:
        common_prime &= set(pf.keys())

    gcf = 1
    for prime in common_prime:
        m = sys.maxsize
        for pf in prime_factorize:
            m = min(m,pf[prime])
        gcf = gcf * (prime ** m)

    return gcf

def findLCM(nums):
    gcf = findGCF(nums)
    lcm = gcf
    for num in nums:
        lcm *= int(num/gcf)
    return lcm

def mainERM():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")

    numA = int(str_numA)
    numB = int(str_numB)

    nums = [numA,numB]    
    gcf = findGCF(nums)
    lcm = findLCM(nums)

    print("Greatest Common Factor: " + str(gcf))
    print("Lowest Common Multiple: " + str(lcm))

mainERM() """

# ----4.形塑出物件導向「強化」、「可讀性」Weak ----
# 問題: 
# - 剛剛的程式碼當中的checkPositiveInteger(num), primeFactorize(num), findGCF(nums), findLCM(nums)函數其實都是實現同一個目標—因式計算，但卻是被寫成一個一個獨立的函數，這裡的內聚性還可以再更好。
# - checkPositiveInteger(num), primeFactorize(num)並不是用來實現主要的目的，而只是實現目的過程中，為了避免重複而產生的，這樣寫很容易讓人不清楚什麼是重要的函數，而什麼只是中繼的函數，這裡的「可讀性」應該還可以再提升。
""" 
應對:
我們需要一個「物件」，這個「物件」能夠保有屬於它的變數，儲存nums等參數，變數可以是對外公布的，也可以是私有的。
另外,這個「對象」擁有屬於它的函數方法，而方法一樣可以是對外公布的，也可以是私有的，所以我們可以公布findGCF(nums), findLCM(nums)，而私有化 checkPositiveInteger(num), primeFactorize(num)。
我們使用「藍圖」去建構「物件」的模版，再由「藍圖」配合不同的輸入參數去生成一個一個獨立的「物件」，以因應不同的狀況。"""

import sys
class Calculation:
    def __init__(self,nums):
        self.__nums = nums
        for num in self.__nums:
            self.__checkPositiveInteger(num)

    def __checkPositiveInteger(self,num):
        if (not isinstance(num,int)) or (num<=0):
            raise ValueError("invalid positive integer: "+str(num))

    def __primeFactorize(self,num):
        prime_factorize = dict()
        i = 2
        while(num > 1):
            if num % i == 0:
                prime_factorize[i] = prime_factorize.get(i,0) + 1
                num /= i
            else:
                i += 1
        return prime_factorize

    def findGCF(self):
        prime_factorize = list()
        for num in self.__nums:
            prime_factorize.append(self.__primeFactorize(num))

        common_prime = set(prime_factorize[0].keys())
        for pf in prime_factorize[1:]:
            common_prime &= set(pf.keys())

        gcf = 1
        for prime in common_prime:
            m = sys.maxsize
            for pf in prime_factorize:
                m = min(m,pf[prime])
            gcf = gcf * (prime ** m)

        return gcf

    def findLCM(self):
        gcf = self.findGCF()
        lcm = gcf
        for num in self.__nums:
            lcm *= int(num/gcf)
        return lcm

def mainERMW():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")

    numA = int(str_numA)
    numB = int(str_numB)

    nums = [numA,numB]
    calc = Calculation(nums)
    gcf = calc.findGCF()
    lcm = calc.findLCM()

    print("Greatest Common Factor: " + str(gcf))
    print("Lowest Common Multiple: " + str(lcm))

print(calc := Calculation([30,70])) # <__main__.Calculation object at 0x0000000002632F70>
numgcf = Calculation([30,40,60]).findGCF()
numlcm = Calculation([30,40,60]).findLCM() # ! 720也是錯的阿
print(numgcf)
print(numlcm)
