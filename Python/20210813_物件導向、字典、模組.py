# @link [學Python基礎物件導向看這一篇文章就夠了【全網首推】 - tw511教學網](https://tw511.com/a/01/35474.html) at 2021-08-12T19:52:43.
# dir內建函數
""" 序號方法名	             型別作用
01	__new__	方法	建立物件時，會被 自動 呼叫
02	__init__方法	物件被初始化時，會被 自動 呼叫
03	__del__	方法	物件被從記憶體中銷燬前，會被 自動 呼叫
04	__str__	方法	返回物件的描述資訊，print 函數輸出使用
提示 利用好 dir() 函數，在學習時很多內容就不需要死記硬背了
"""
# test = 5
# print(dir(test))

# > 提示：在計算機中，通常使用 十六進位制 表示 記憶體地址
# %d 可以以 10 進位制 輸出數位
# %x 可以以 16 進位制 輸出數位

# 在 Python 中，要給物件設定屬性，非常的容易，加個點就好了，但是不推薦使用，建議建在類里
""" 
當使用 類名() 建立物件時，會 自動 執行以下操作：
1. 為物件在記憶體中 分配空間 —— 建立物件
2. 為物件的屬性 設定初始值 —— 初始化方法(init) 
"""
""" class Cat:
    def __init__(self, name, love, age):
        self.name = name
        self.love = love
        self.age = age
    def eat(self):
        print(f'Cat {self.name} is eating food.')

cat01 = Cat('Tom','9','12')
cat01.eat()
 """

# ----物件導向封裝----
# ----小明愛跑步----
""" class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"我的名字叫 {self.name} 體重 {self.weight:.2f} 公斤"

    def run(self):
        print(f"{self.name} 愛跑步，跑步鍛鍊身體")
        self.weight -= 0.5

    def eat(self):
        print(f"{self.name} 是吃貨，吃完這頓再減肥")
        self.weight += 1

xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
print(xiaoming) """

# ----存放傢俱----
""" class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"[{self.name}] 佔地面積 {self.area:.2f}"

# 1. 建立傢俱
bed = HouseItem("席夢思", 4)
chest = HouseItem("衣櫃", 2)
table = HouseItem("餐桌", 1.5)

# print(bed)
# print(chest)
# print(table)

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩餘面積預設和總面積一致
        self.free_area = area
        # 預設沒有任何的傢俱
        self.item_list = []
        self.item_list_dict = {}

    def __str__(self):
        return f"戶型：{self.house_type}\n總面積：{self.area} (剩餘：{self.free_area})\n傢俱：{self.item_list_dict}"

    def add_item(self, item):
        print(f"要新增 {item}")
        # 1. 判斷傢俱面積是否大於剩餘面積
        if item.area > self.free_area:
            print(f"{item.name} 的面積太大，不能新增到房子中")
            return
        # 2. 將傢俱的名稱追加到名稱列表中
        self.item_list.append(item.name)
        self.item_list_dict = {i: self.item_list.count(i) for i in self.item_list}
        # 3. 計算剩餘面積
        self.free_area -= item.area
...

# 2. 建立房子物件
import random
my_home = House("兩室一廳", 60)
items = [bed,chest,table]  #! item is not str

def rand_buy(house,buy_num):
    for _ in range(buy_num):
        house.add_item(random.choice(items))
rand_buy(my_home,30)
print(my_home) """

# ----封裝----
""" 
1.封裝 是物件導向程式設計的一大特點
2.物件導向程式設計的 第一步 —— 將 屬性 和 方法 封裝 到一個抽象的 類 中
3.外界 使用 類 建立 物件，然後 讓物件呼叫方法
4.物件方法的細節 都被 封裝 在 類的內部 
"""
# 在定義屬性時，可以將 None 賦值給任何一個變數

# ----士兵突擊案例----
# ! 變數為物件時，可以輕易導入到其他任何變數內
# ! 像是ak47可以放到人身上
# *需求
""" 
槍        的名 叫AK47
槍   能夠 發射 子彈(數量減少)
槍   裝填 裝填 子彈(數量增加) 
士兵      的名 叫 Henry
士兵      的槍 有一把 叫AK47
士兵 可以 開火
"""
# *1.1 開發槍類
# *shoot 方法需求
# *fire 方法需求

""" class Gun:
    def __init__(self,name,bullet_full,bullet_count):
        self.name = name
        self.bullet_full = bullet_full
        self.bullet_count = bullet_count
        
    def shoot(self):
        self.bullet_count -= 1
    
    def reload(self):
        self.bullet_count = self.bullet_full
        

class Soldier:
    def __init__(self,name,*guns):
        self.name = name
        self.gun = []
        for gun in guns:
            self.gun.append(None or gun)

    def __str__(self):
        return f'''            士兵名:{self.name}
            槍:{(gun := {gun.name:gun.bullet_count for gun in self.gun})}  
        '''
# 槍:{(gun := {gun.name: gun.bullet_count for gun in self.gun})} # 海象+生成好厲害喔!

# 從第一把有子彈就開始射擊，射一發
    def fire(self):
        for gun in self.gun:
            if gun.bullet_count == 0:
                print('No bullet to shoot!')
                ru_re = input('Reload? Yes or No?')
                if ru_re == 'Yes':
                    gun.reload()
                return
            gun.shoot()
            print('砰')
            break


ak47 = Gun('AK47',12,12)
smGreedy = Gun('SmallGreedy',6,6)
Henry = Soldier('Henry',ak47,smGreedy)
Tom = Soldier('Tom')

# 發射Fire!
shoot_num = 3
for _ in range(shoot_num):
    Henry.fire()

print(Henry) """

# ----身份運運算元: is or is not----
""" 
is 與 == 區別：
is 用於判斷 兩個變數 參照物件是否為同一個 
== 用於判斷 參照變數的值 是否相等
> 提示: 在 Python 中針對 None 比較時，建議使用 is 判斷 
"""

# ----私有屬性和私有方法----
""" class Woman:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # 私有屬性
    
    def __secret(self): # 私有方法
        print(f'My age is {self.__age}')

woman01 = Woman('Maggy',22)
print(woman01.name)
# print(dir(woman01))        
print(woman01._Woman__age)
woman01._Woman__secret() """

# ----字典----
# ! =等式都直接用key的字即可，不用轉字串
# ----建立----
""" # 字面量語法
scores = {'駱昊': 95, '白元芳': 78, '狄仁傑': 82}
# 構造器語法
items1 = dict(one=1, two=2, three=3, four=4)
# 通過zip函式將兩個序列壓成字典 #*沒有對應到的會直接忽略
items1 = dict(zip(['a', 'b', 'c'], ['12','34','56'])) 
items2 = dict(zip(['a', 'b', 'c'], '123')) # {'a': '1', 'b': '2', 'c': '3'}
# 生成式，推導式語法
items3 = {num: num ** 2 for num in range(1, 10)}
# print(items1,items2,items3) """

# ----獲取----
# !對所有鍵值對進行遍歷
# !事實上，這邊的key=x，填甚麼都可以，都會對應到key
scores = {"駱昊": 95, "白元芳": 78, "狄仁傑": 82}
# for key in scores:
#     print(f'{key}: {scores[key]}')
# # for x in scores:
# #     print(f'{x}')
# 海象生成
# print (f'{(score:={key:scores[key] for key in scores})}')

# 鍵 -> 值
# print(scores['駱昊'])
# if '武則天' in scores:
#     print(scores['武則天'])
# get()，沒有get就返回None
# print(scores.get('武則天', 60)) # clr: 設定預設值，數字60的效果? 找不到會回傳60，預設為None

# clr: 特殊類型，只能用來sorted嗎? 在前面加上set/list轉成可以用的物件
# print(scores.keys()) # type: <class 'dict_keys'>
# print(scores.values()) # type: <class 'dict_values'>


# ----更新，新增，刪除----
# 更新字典: 沒有會自動新增
# scores['諸葛王朗'] = 71
# scores.update(冷麵=67, 方啟鶴=85, 駱昊=70)

# 刪除字典中的元素
# print(scores.popitem()) # pop從最後面開始刪除，返還值為tuple (key,value)
# print(scores.pop('白元芳')) # 刪除特定key:value，返還值為key的value #? 數字75的效果?? scores.pop('白元芳',75)

# 清空字典
# scores.clear()
# print(scores)

# ----模組----
# @link [Python - 模組與包 | IT人](https://iter01.com/510366.html) at 2021-08-13T13:17:50.
# @link [解析Python模組(Module)和套件(Package)的概念](https://www.learncodewithmike.com/2020/01/python-module-and-package.html) at 2021-08-13T13:49:40.
# @link [Python Module 模組的載入與使用 By 彭彭 - YouTube](https://www.youtube.com/watch?v=Et0DjY2cGiE) at 2021-08-13T11:00:04.
# @link [python模組和包_實用技巧_程式人生](https://www.796t.com/article.php?id=205211) at 2021-08-13T12:41:28.
# ----匯入、呼叫自訂模組---
# 01.利用sys增加讀取路徑，來呼叫
# import sys
# sys.path.append("modules") # 新增module要掃描的路徑 #!注意 此相對路徑代表的是vscode的開啟資料夾位置開始算起(工程目錄?)
# print(sys.path) # 列出module會掃描的路徑，絕對路徑的話老實說沒甚麼用...
# import newfunction as nf
# nf.sayhello('Rock')

# ?? 上層的modeules怎麼辦
# 02.鏈式呼叫 #! 相對於執行的py路徑，好用! 但有可能很長，且上一層不知道怎麼用
# import modules.newfunction as nf
# nf.sayhello('Rock')

# ----import細節----
""" 當匯入一個模組，Python解析器對模組位置的搜尋順序是：
1. 當前目錄
2. 如果不在當前目錄，Python則搜尋在shell變數PYTHONPATH下的每個目錄。
3. 如果都找不到，Python會察看預設路徑。UNIX下，預設路徑一般為/usr/local/lib/python/ 
"""
# * import : 完全匯入，選擇[模組或包] (模組內的變數、函式名、類名，用時記得鏈式呼叫)
# * from...import... : 部分匯入，import選擇[模組(from包的概念)、變數、函式名、類名]引入 (若用*代表所有物件，要小心Method Overriding的風險)
# * as : 隨時可用的好東西
# * sys.path 得模組路徑讀取順序，dir()得模組內屬性跟方法

# %%
rock1 = 20
import mymodules.newfunction as nf
print(rock1) # 這裡則是引用本篇的rock1
print(nf.rock1) # 因為特別引用nf的rock1，不會跟本篇的rock1衝突


# %%
# rock1 = 20
# from modules.newfunction import *
# print(rock1) # 因為名稱一樣，他會引用nf的rock1，所以會覆蓋掉本篇的rock1

# from modules.newfunction import rock1
# print(rock1)
# from modules import newfunction
# print(newfunction.rock1)

# from 包，必須在__init__.py檔案中新增__all__ = []，控制允許匯入的模組列表
# ! python 3.3+支援隱式名稱空間包，允許它創建不帶__init__.py檔的包，前提是只適用於空的__init__.py
# ! 若有需要運行特定的初始化腳本，那就無法省略的
# from modules import newfunction as nf #?? 如果不加 import newfunction，不知道為什麼就是不行
# nf.sayhello('Rock')

# ----dir()獲取屬性與方法----
""" import modules.newfunction as nf
print(dir(nf)) # ['__builtins__', '__cached__',..., 'distance', 'rock1', 'sayhello']
print(nf.dir_remodule(dir(nf))) # 去掉系統預設方法
"""

# 模組的一些常用屬性(Attribute)，別忘記當前執行的.py檔案的__name__的值自動被設定為"__main__"
""" import modules.newfunction as nf
print(__name__) #__main__
print(nf.__name__)  # 模組名稱 # modules.newfunction
print(nf.__package__)  # 套件名稱 # modules
print(nf.__file__)  # 模組的檔名及路徑 #絕對路徑g:\my_python_project\2021_my_python\modules\newfunction.py
 """

# ----將模組當作腳本來執行(Executing a Module as a Script)----
# * 如果希望主程式不執行，模組當腳本運行的部分可以加上一個條件(等於是模組可以內部測試不用砍掉)
# @link [Python小技巧#1：__name__ == '__main__' 是做什么用的？ - YouTube](https://www.youtube.com/watch?v=lOfYjXsziD8) at 2021/9/1
""" 
使用: 在模組(Module)加上了判斷式if __name__ == "__main__": TestFunction()
效用: 當其他py引入(import)模組時，不會跑兩次TestFunction，
因為調用時的__name__會變成import的py檔名，可能再加模組名，並不等於__main__
"""
