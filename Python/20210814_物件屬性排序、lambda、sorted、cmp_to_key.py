from operator import itemgetter
from operator import neg

# ----Python獲取物件屬性的4種方法----
# 學生與期中考成績


class Student:
    def __init__(self, id, name, midexam):
        self.id = id
        self.name = name
        self.midexam = None or midexam  # ? None讀出來是()，不是None嗎? 甚麼時候是呢?

    def __str__(self):
        midexam_dict = {key: self.midexam[key] for key in self.midexam}  # {字典生程式}
        # 也可以用海象表達成績 (midexam_dict:={key:self.midexam[key] for key in self.midexam})
        return f"""{self.id=}, {self.name=} {midexam_dict=}"""  #! 對於後台表達，要習慣{=}


subjects = ["Chinese", "English", "Math", "Physics", "Chemistry"]

""" 
scores01 = [80,90,91,88,75]
mid01 = dict(zip(subjects,scores01))
student01 = Student(1,'Henry',mid01)
# 方法一：使用屬性運算子
print(student01.name)

# 方法二：通過屬性字典__dict__
print(student01.__dict__['name'])

#? 方法三：通過getattr函式
print(getattr(student01,'name'))

#? 方法四：operator.attrgetter (可以多重查找) 
import operator
op = operator.attrgetter('name')(student01)  # !真的長的超奇怪的
print(op)
op = operator.attrgetter('name','id','midexam')(student01)
print(op) 
"""


# ----Python物件排列sort的方法----
# *方法四還可以用於物件的排序
""" from operator import attrgetter
scores01 = [80,90,91,88,75]
scores02 = [99,55,45,33,35]
scores03 = [75,45,91,88,75]
scores04 = [65,75,80,80,70]
mid01 = dict(zip(subjects,scores01))
mid02 = dict(zip(subjects,scores02))
mid03 = dict(zip(subjects,scores03))
mid04 = dict(zip(subjects,scores04))
student_list = [
    Student(1,'Henry',mid01), 
    Student(2,'Meggy',mid02), 
    Student(3,'Ming',mid03), 
    Student(4,'Ling',mid04)
    ]
# r = sorted(student_list, key=attrgetter('name')) # 名字排列，attrgetter原始方式，返回一個可呼叫物件，該物件從其運算元中獲取屬性。
# r = sorted(student_list, key=lambda x: x.name) # 名字排列，lambada方式
r = sorted(student_list, key=lambda x: x.midexam['Chinese'], reverse=True) # 選定Chinese來排列，太強了吧!
for i in r:
    print(i)  """

# // print((lambda x: student_list[0].midexam['Chinese']))

# ----sorted vs sort----
# *sorted: "返回"已排序的列表，"不更動"原始列表
# *sort:   "不返回"任何值，"更改"原始列表，僅支援列表
# 皆支援 reverse=True 的參數
# ?? "不返回"任何值 = None對嗎?
# 排序字元，會先將字元轉ASCII碼，可以用ord()查字元的ASCII碼
# (ASCII對應碼「 0 對應 48(十進位)、'A'對應 65(十進位)、'a'對應 97(十進位)」。)
""" 
listing = [5, 1, 4, 7, 2]
listing.sort()
print(listing.sort())  # None
print(listing)  # [1, 2, 4, 5, 7]

listing2 = [5, 1, 4, 7, 2]
print(sorted(listing2))  # [1, 2, 4, 5, 7]
print(listing2)  # [5, 1, 4, 7, 2]
 """

# @link [Python排序應用(教學篇)|文章分享|海獅程式](https://icoding.com.tw/articles/python-tutorial-understanding-sorting.php) at 2021-08-13T23:13:35.
# dict資料型態
""" data_d = {"b": 5, "c": 9, "g": 1, "i": 11, "e": 3, "a": 2}

# *字典dict使用key來比對排序(預設值)，只有key拿來比
data_d_s = sorted(data_d)
print("排序後資料：", data_d_s)  # ['a', 'b', 'c', 'e', 'g', 'i']

# *字典dict使用values來比對排序，只有value拿來比
data_d_s = sorted(data_d.values())
print("排序後資料：", data_d_s)  # [1, 2, 3, 5, 9, 11]

# *字典dict使用item來比對排序，預設key(x[0])來比，利用lambda可以用value(x[1])來比
data_d_s = sorted(data_d.items(), key=lambda x: x[1])
print("排序後資料：", data_d_s) """

# ----其他key排序變化應用----
# key指定一個參數的函數
# data_k_1 = ["b", "Boy", "Apple", "a"]

# print("[小寫]比對排序後的資料：", sorted(data_k_1, key=str.lower))
# print("[小寫]比對排序後的資料：", sorted(data_k_1, key=lambda x: str(x).lower()))

# print("[長度]比對排序後的資料：", sorted(data_k_1, key=len, reverse=True))
# print("[長度]比對排序後的資料：", sorted(data_k_1, key=lambda x: len(x)))

# ----多欄位來排序(兩個元素是可以互相比較的前提)----
# @link [關於內建函式sorted，你必須知道的10個知識點_FooFish的筆錄 - MdEditor](https://www.gushiciku.cn/pl/2xrA/zh-tw) at 2021-08-14T01:00:28.


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    # def __str__(self):
    #     return f'{self.name=}, {self.grade=}, {self.age=}'


#! __repr__ vs __str__
""" 
單獨print一個學生的話，資料會是__str__的return優先於__repr__
如果print學生清單的話，只有__repr__的return列印得出來
__str__的部分會變成記憶體位置 
"""
""" student_objects = [
    Student("john", "A", 15),
    Student("jane", "B", 12),
    Student("lily", "A", 12),
    Student("dave", "B", 10),
]
print(sorted(student_objects, key=lambda x: (x.age)))
# [('dave', 'B', 10), ('jane', 'B', 12), ('lily', 'A', 12), ('john', 'A', 15)]
print(sorted(student_objects, key=lambda x: (x.age, x.grade))) # 多重排序
# [('dave', 'B', 10), ('lily', 'A', 12), ('jane', 'B', 12), ('john', 'A', 15)] """

# ----自定義來排序----
# *在Python3中，字串與數值是不能比較的，而Python2中任何型別都可以比較，這是兩個版本中一個很大的區別
# Python2中的sorted可以直接指定cmp關鍵字引數，cmp=compare 來實現
# 需要定義的簡單例子:字串與數值的比較
nums = [2, 1.5, 2.5, "2", "2.5"]
# print(sorted(nums))
# # TypeError: '<' not supported between instances of 'str' and 'int'

# ?? 使用 functools 模組中的 cmp_to_key 來指定比較函式
# @link 詳細def參看 [如何排序 — Python 3.9.6 說明文件](https://docs.python.org/zh-tw/3/howto/sorting.html) at 2021-08-14T07:50:08.
""" import functools


def compare(x1, x2):
    if isinstance(x1, str): # isinstance(object, classinfo)
        x1 = float(x1)
    if isinstance(x2, str):
        x2 = float(x2)
    return x1 - x2  # 猜測:預設用lt再比較 x1 < x2，所以 x1-x2 < 0，來代表


print(sorted(nums, key=functools.cmp_to_key(compare))) # [1.5, 2, '2', 2.5, '2.5'] """

# ----對於集合構成的列表----
# ----@itemgetter----
# !注意，operator.itemgetter函數獲取的不是值，而是定義了一個函數，通過該函數作用到物件上才能獲取值
""" from operator import itemgetter

a = [1, 2, 3]
b = itemgetter(1)
print(b(a))  # 1
b = itemgetter(1, 0)
print(b(a))  # (1,2)

# 測試結果: 不同數量的集合，也能排序，但不能少於排序量itemgetter
studentslist = [("zhang", 1), ("wang", 3), ("li", 4), ("li", 1)]  # ?? 加個a,b多重排序的效果就消失了?

# operator引用，key=itemgetter(1)
from operator import itemgetter

studentslist_s = sorted(studentslist, key=itemgetter(1))
print("排序後資料：", studentslist_s)
# 排序後資料： [('zhang', 1), ('li', 1), ('wang', 3), ('li', 4)]
# 也可以多重(多級)排序
studentslist_s = sorted(studentslist, key=itemgetter(0, 1))
# studentslist_s = sorted(studentslist,key=lambda x: (x[0], x[1]))
print("排序後資料：", studentslist_s)
# 排序後資料： [('li', 1), ('li', 4), ('wang', 3), ('zhang', 1)] #?? [('lia', 4), ('lib', 1), ('wang', 3), ('zhang', 1)
 """

# *itemgetter進階
""" alist = [
    ("2", "3", "10"),
    ("1", "2", "3"),
    ("5", "6", "7"),
    ("2", "5", "10"),
    ("2", "4", "10"),
]
# 多级排序，先按照第3个元素排序，然后按照第2个元素排序：
print(sorted(alist, key=itemgetter(2))) # !注意，字串比較:所以 '10' < '3'
print(sorted(alist, key=lambda x: itemgetter(2, 1)(x)))
print(sorted(alist, key=lambda x: tuple(map(int, itemgetter(2, 1)(x))))) # !注意 map object不能被lambda接受 """

# *物件排序
# operator引用，key=attrgetter('age')
# operator引用，key=attrgetter('grade', 'age')

# ----其他排序----
# *通過定義__lt__（）方法，可以很容易地為類添加標準排序順序
# ! 這個前提看起來定要有class先，看好像也可以別的方式來應用
""" class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age))   # sort by age 10 12 15
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
Student.__lt__ = lambda self, other: neg(self.age) < neg(other.age) #! sort by -age -15 -12 -10
print(sorted(student_objects))
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)] """

# *鍵函數還可以訪問外部資源
""" students = ['dave', 'john', 'jane']
newgrades = {'john': 7, 'jane': 1, 'dave': 3} # 權重1 3 7 排序 students，但不需要key=students的東西
print(sorted(students, key=newgrades.__getitem__)) # ['jane', 'dave', 'john']
# TODO 這樣不就可以創造預先設定好的key? 但要怎麼做呢
 """
# 其他參考連結
# @link 簡單明瞭 [關於內建函式sorted，你必須知道的10個知識點_FooFish的筆錄 - MdEditor](https://www.gushiciku.cn/pl/2xrA/zh-tw) at 2021-08-14T09:33:01.
# @link [python sort、sorted高階排序技巧 | 程式前沿](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/373191/) at 2021-08-14T09:25:44.
