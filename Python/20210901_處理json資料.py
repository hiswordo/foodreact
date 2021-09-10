

# @link [Python 操作 JSON 的 9 个示例 - 知乎](https://zhuanlan.zhihu.com/p/146762139) at 2021/9/2
# ----Json----
# 輕量級的資料交換格式。卻跟JS無關，人和機器都能讀懂的文件
# 文字格式: JSON的數據兩邊都有單引號，JSON數據是以字符串形式表示
# 特性:
""" 
1. 字串必須使用 雙引號包圍
2. 可以在任何值前後插入空白 
"""
# 物件特性:
""" 
1. {} 括起來的一個集合，每一項都包含名稱和值
2. 六種值的選擇: 物件，陣列，字串，數字，布林值和null 對應 python的 *"dict、list/tuple...、none"
3. 名稱/值 對沒有固定的順序，可以是任意順序
4. 可以支援無限層的巢狀，但是為了保證處理的高效性，請儘量保持結構的扁平性(巢狀不要太多層）
 """
import json
dictBook = {"K": 17, "S": 18, "Y": "十九"}
print(dictBook)

# ----01.編碼-序列化:把python obj轉爲JSON字串 (注意key變成雙引號)----
# dumps(obj, **kwargs)
# ensure_ascii=True/False # False的話可以接受中文，否則只接受ASCII表的數據類型
# sort_keys=True 按照 key 來排序
# encoding="utf-8" 預設值
# separators=(",", ": ") 預設值(也可以移除:的空格，排版有差一點) 也可以separators=(",", " = ")給js用的
jsonBook = json.dumps(dictBook, ensure_ascii=False)
print(jsonBook)
# True: {"K": 17, "S": 18, "Y": "\u5341\u4e5d"}
# False: {"K": 17, "S": 18, "Y": "十九"}

# ----02.解碼-反序列化:JSON格式轉化爲Python的數據：----
backToDictBook = json.loads(jsonBook)
print(backToDictBook)

# ----03.寫入 與 讀取 json檔案----
# dump and load 少了s，就讀檔案跟寫檔案，其他一樣
import json

sampleJson = {"id": 1, "name": "value2", "age": 29}
filename = "res/json_example.json"
# 寫入
with open(filename, "w") as write_file:
    # *indent=4,會幫忙排版，但排版後會增加儲存所需的空間跟傳輸量，通常是不建議在儲存時做排版的。
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")
# 讀取
# ??"w+"是不行的 => json.decoder.JSONDecodeError
with open(filename, "r") as read_file:
    data = json.load(read_file)
print(f"reading Json:{data}")


# -----04.class 對象 轉 Json----
import json
from json import JSONEncoder


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class Bicycle:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price


# @link [Python json dumps custom type - 石頭閒語](https://www.rocksaying.tw/archives/12153263.html) at 2021/9/2
# ?? JSONEcoder到底用來幹嘛
# default keyword argument
""" 
以 default 鍵值參數指定自定型別資料的序列化函數或方法。該函數或方法必須接受一個參數。
當你指定 default 鍵值參數時，json.dumps() 仍將使用預設的 json.JSONEncoder 擷取與轉換資料內容。但是當資料內容的型別是 json.JSONEncoder 所不支援的自定型別時，它就會將這個資料丟給 default 指定的方法處理。 
"""


class ObjEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


newVehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
newBicycle = Bicycle("Gogoro", 150, 12000)
print(newVehicle.__dict__)  # {'name': 'Toyota Rav4', 'engine': '2.5L', 'price': 32000}

# cls keyword argument
""" 
另一種處理自定型別轉換動作的方式是使用 cls 鍵值參數。cls 鍵值參數必須指定一個以 json.JSONEncoder 為基礎類別的子類別，而且至少應覆寫 default 方法。

當你指定 cls 鍵值參數，json.dumps() 將直接使用你指定的類別處理資料轉換動作。

大多數情形，我們只需要指定鍵值參數 default 為我們自定的序列化方法即可。當你想要改變 Python json 模組的預設序列化行為時，你才需要使用鍵值參數 cls 自定 JSONEncoder 子類別的方式。 
"""
print("Encode Vehicle Object into JSON")
data1 = json.dumps(newVehicle, cls=ObjEncoder)
data2 = json.dumps(newBicycle, cls=ObjEncoder)
print(data1)
print(data2)

# ??如果用函數的方式，來轉json，這樣不好嗎? 目前感覺是因為可讀性比較高
def ObjEncode(obj):
    return obj.__dict__


data3 = json.dumps(ObjEncode(newBicycle))
print(data3)

# ---- 05.json轉回class對象-----
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def vehicleDecoder(obj):
        return Vehicle(obj['name'], obj['engine'], obj['price'])

vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
           object_hook=vehicleDecoder)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)

# ---- 06.判斷 Json 格式是否正確----
import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid", isValid)


# ---- 07.獲取 JSON 中key為name的所有值----
import json

sampleJson = """[
   {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },
   {
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }
]"""

data = []
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data]
print(dataList)