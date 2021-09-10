
# @link [【python】繼承 inheritance 概念介紹 - YouTube](https://www.youtube.com/watch?v=JdLLacLF5Wc&list=PLRjgE3pAnTIKu2Mr1kiCanx_vnMFD97Ac&index=22) at 2021/8/16
# name = "Johnny"
# age = 87
# Is_male = True
# Listtest = [0,1,2]
#print("my name is \"" + name + "\", and \nI am " + str(age) + " years old.")

# # --------**字串相關function**--------
# phrase = "Hello Motto"
# # print(phrase.lower().islower())
# print(phrase[0] + phrase[1]) #無空格
# print(phrase[0], phrase[1], age, Is_male, Listtest) #連結時中間會有空格，而且可以連結不同型態的資料
# index 第一個相同的字母
# print(phrase.index("e"))
# print(phrase.replace("l","L"))

# # --------**數字相關function**--------
number_save = 38
# 整數除法，省略小數點後 print(5//3) = 1
# 取餘數 print(5%3) = 2
# 轉字串 str(37) = "37"
# 絕對值 abs(-38) = 38
# 2的4次方 pow(2,4) = 2^4
# 找出最大數 max(3, 5, 7) = 7
# 四捨五入 round(4.6) = 5
# from math import *
# 無條件捨去 floor(4.3) = 4 
#   slo.2: 4.3//1 or slo.3: int()
# 無條件進位 ceil(5.1) = 6
# 開根號 sqrt(4) = 2

# # --------**輸入數字的計算機**--------
# # 不要忘記! input得到的是string字串
# number_01 = input("welcome! give a number: ")
# number_02 = input("another: ")
# print(int(number_01) + int(number_02))
# # 有小數點的計算
# print("Answer is "+ str(int(float(number_01) + float(number_02))))

# # --------**List的用法(objects inside)**--------
# things = [90, "String", True, 30, 40]
# # print(things[-1]) # 倒數第1位
# print(things[3:5]) # [3][4]的意思不含[5] (第4、5位)
# print(things[1:]) # 第2位~到結束 or 從開始到n+1位
# phrase = "Hello Motto"
#         # 0123456789
# print(phrase[0:5])
# print(phrase[6:])

# score = [30, 60, 50, 40, 50]
# morescore = ["七十", "八十", "九十"]
# score.extend(morescore) # 不能在print裡面運作的原因??
# score.append(90) # 增加新的最後一位
# score[-2] = 0 # 替換某一格
# score.insert(2, "我是第二位") #插入在第二位
# score.remove(60) #去除60值的物件
# score.clear() # score = []
# score.pop() # 移除最後一位
# score.sort() # 由小到大排列，有混值時不能用
# score.reverse() #反過來
# scoreposition = score.index(40) # 那要怎麼一次找出很多個位置呢??
# print(scoreposition) 
# scorecount = score.count(50)
# print(scorecount)

# # 因為是容器，所以可以放任何資料型態，再放一個清單也可以
# listbox = [1, 2, [7, 9, 10]]
# print(listbox[2][0])

# # --------**元組tuple**--------
# # 操作幾乎等同list
# # 一旦被創建，就無法修改，永來保護資料，ex座標位置
# location = (123.45, 110.22)
# print(location)

# --------**自創函式**--------
# 函式定義，記得要冒號，注意tab空白後的才有用，return非常重要!
# 函式呼叫
# 傳入為數字的話，字串無法用+號相加
# def sayhello(name, age):
#     print("hello " + name + ", u r " + str(age)) 
# sayhello("Johnny", 87)

# def addnum(num1, num2):
#     print(num1+num2)
# addnum(3, 4)

# def addnumber(numb1, numb2):
#     print(numb1+numb2)
#     return 10  # addnumber(3, 4)=10，如果沒定義的話，會等於None
#     #return numb1+numb2
#     #並且只要遇到return，即為終點，以下都不會再執行
#     #return的用處是通常出來的值還要再做其他運算，應該還有別的意義吧???
# value = addnumber(3, 4)
# print(value)

# def nonedef(nb1, nb2):
#     print("您好")
#     return None # 有寫跟沒寫一樣
# nore = nonedef(3, 4)
# print(nore)


# --------**if判斷句**--------
# 雙判斷語句應該有好一點的方法??
# random的用法還不錯簡單
# import random
# hungry = random.randrange(0,100)
# hungry_percent = " 飢餓程度:" + str(hungry) + "%"
# rainy = random.choice([True, False])

# if hungry>=80 and not(rainy):
#     print("我要去吃吃到飽" + hungry_percent)
# elif hungry>=60 and not(rainy):
#     print("好想吃大餐" + hungry_percent)
# elif hungry>=35 and not(rainy):
#     print("附近吃一下吧" + hungry_percent)
# elif hungry>=50 and rainy:
#     print("雖然肚子很餓，但在下雨來睡覺吧" + hungry_percent)
# else:
#     print("肚子不會餓，來睡覺吧" + hungry_percent)

# 製作函式找出最大值
# from math import *
# def max_num(num1, num2, num3):
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
# print("I'll tell u the biggest number!")
# number01 = float(input("Give me the 1st number: "))
# number02 = float(input("Give me the 2nd number: "))
# number03 = float(input("Give me the last number: "))
# given_number = max_num(number01, number02, number03)
# print(str(floor(given_number)) + " 為最大值")


# --------**容器字典dic**--------
# dic = {"蘋果":"Apple", "貓咪":"Cat", "狗":"Dog"}
# print(dic["蘋果"])


# --------**While迴圈**--------

# i=5
# while 0<i<=5:
#     print(i)
#     i -= 1 #運算變化  i = i - 1
# print("End of while")


# 猜數字遊戲 我的寫法
# guessnum = None  # 還不知道可以先給None
# secret_num = random.randrange(1,100)
# urguess_lives = 3
# while guessnum != secret_num and urguess_lives > 0:
#     print("您還剩下 " + str(urguess_lives) + " 次猜的機會")
#     guessnum = int(input("猜猜我是誰? "))
#     urguess_lives -= 1
#     if guessnum > secret_num:
#         print("猜錯啦! 猜的數字太大了喔")
#     elif guessnum < secret_num:
#         print("猜錯啦! 猜的數字太小了喔")
#     else:  # 如果無論如何他本來就要離開迴圈，也只執行一次，可以省略
#         print("\n恭喜你! 猜對了! 數字就是 "+str(secret_num))
# print("\n機會用光拉，太遜了吧! 數字其實是 "+str(secret_num))

# 猜數字遊戲 老師的寫法
# import random
# guessnum = None
# secret_num = random.randrange(1,100) #最高到99的意思
# guess_count = 0
# guess_limit = 5
# out_of_limit = False
# while guessnum != secret_num and not(out_of_limit):
#     guess_count += 1
#     if guess_count <= guess_limit:
#         print("您猜了 " + str(guess_count-1) + " 次! 還剩下" + str(guess_limit-guess_count+1) + "次機會")
#         guessnum = int(input("猜猜我是誰? "))
#         if guessnum > secret_num:
#             print("猜錯啦! 猜的數字太大了喔")
#         elif guessnum < secret_num:
#             print("猜錯啦! 猜的數字太小了喔")
#     else:
#         out_of_limit = True
# if out_of_limit:
#     print("\n機會用光拉，太遜了吧! 數字其實是 "+str(secret_num))
# else:
#     print("\n恭喜你! 猜對了! 數字就是 "+str(secret_num))


# --------**For迴圈**--------
# for num in range(2,7): #[2,3,4,5,6] 
#     print(num)

# 次方測試
# basenum = 3
# uppernum = 4
# outcomenum = 3
# while uppernum-1 > 0:
#     outcomenum *= basenum
#     uppernum -= 1
# print(outcomenum)

# # 製作函式pow
# def power(basenum, pownum):
#     outcomenum = basenum
#     for numtimes in range(pownum-1): # range(1,3)=range(2)
#         outcomenum *= basenum
#     return outcomenum   #小心return就跳出def了喔，tab不要在for裡面，會跳出迴圈
# print(power(2,5))


# --------**2維列表、巢狀迴圈**--------
# num = [
#     [0,1,2],
#     [3,4,5],
#     [6,7,8],
#     [9]
#     ] #[[0,1,2],[3,4,5],[6,7,8],[9]]
# print(num[3][0]) #第四列第一行
# for row in num:
#     for col in row:
#         print(col)


# --------**檔案的讀取、寫入**--------
# 絕對(\號要換成/)跟相對路徑，並且記得開啟後關閉，才不佔系統資源
# 還有讀寫模式r+
# file = open("123.txt", "r") #放到file裡面，完整寫法等同 file = open("./123.txt", mode="r") 相對路徑與mode 
# print(file.read()) #全部讀出來
# print(file.readline()) #讀一行
# for line in file: #一行一行讀
#     print(line)
# print(file.readlines()) #每行資料放到列表裡面['77\n', '78\n', '79\n', '80\n', '81\n', '82']
# file.close()

# file = open("123.txt", "w")
# file.write("hello") #整個檔案都會被覆蓋
# file = open("123.txt", "a")
# file.write(" Motto") #只有加在後面

# file = open("123.txt", mode="a", encoding="utf-8")
# file.write("\n您好")
# file.close()
# 如果會忘記使用close()，也可以用另外的寫法
# with open("123.txt", mode="a", encoding="utf-8") as file:  #with是甚麼樣的寫法阿??
#     file.write("\n哈~")
# 如果是json
# 讀取要用json.load(檔案物件)
# json.dump(要寫入的資料,檔案物件)


# --------**模組module的使用**--------
# 1.自己的 2.官方的 3.其他人的 (用pip套件管理模組來幫忙)
# https://docs.python.org/zh-tw/3.8/py-modindex.htmlhttps://docs.python.org/zh-tw/3.8/py-modindex.html
# import pytool  # 不需要點副檔名
# import token
# import sys
# import numpy as np
# # print(pytool.name)
# # print(pytool.max_num(20,3,888)) #輸入max_num它會自動幫你產生前面的pytool
# # print(sys.path)


# --------**類別class、物件object **--------
# class phone:
#     def __init__(self,osin,idnumberin,is_waterproofin):
#         self.os = osin
#         self.idnumber = idnumberin
#         self.is_waterproof = is_waterproofin

# phone1 = phone("ios",123,True)
# phone2 = phone("android",456,False)
# print(phone1.os)
# print(phone2.os)

# --------**製作一個問答程式**--------
# import question_tool #整份一起import
# from question_tool import Question
# test = [
#     "1+3=?\n(a) 3\n(b) 4\n(c) 2\n\n",
#     "1 m = ? cm\n(a) 100\n(b) 1000\n(c) 10\n\n",
#     "What's the color of a banana?\n(a) yellow\n(b) black\n(c) orange\n\n",
#     "Which object is red?\n(a) bottle\n(b) water\n(c) crab\n\n"

# ]
# questions = [
#     Question(test[0],"b"),
#     Question(test[1],"a"),
#     Question(test[2],"a"),
#     Question(test[3],"c")
# ]
# print(questions)

# def run_test(questionsinput): #有必要加這個def???
#     score = 0
#     for ques_num in questions:
#         answer = input(ques_num.dscip)
#         if answer == ques_num.ans:
#             score += 1
#     print("u got " + str(score) + " points and u finished " + str(len(questions)) + " questions")
# run_test(questions)


# --------**物件函式**--------
# class phone:
#     def __init__(self,osin,idnumberin,is_waterproofin,pricein):  #self的詳細意義??
#         self.os = osin
#         self.idnumber = idnumberin
#         self.is_waterproof = is_waterproofin
#         self.price = pricein
#     def is_ios(self):
#         if self.os == "ios":
#             return True
#         else:
#             return False
#     def sale_percent(self,sale_price):
#         return (sale_price/self.price)*100

# phone1 = phone("ios",123,True,700)
# print(phone1.is_ios())
# print("About " + str(int(phone1.sale_percent(500))) + "%")

# --------**繼承 inheritance 概念介紹**--------
# from person_info import Person

# class Student(Person):
#     def __init__(self,name,age,school):  #不可省略，他會覆蓋前面的__init__包含裡面重複的部分都會覆蓋掉，如果省略就會用空白取代之
#         self.name = name   
#         self.age = age
#         self.school = school

#     def print_urschool(self):
#         print(self.school)

# student1 = Student("Johnny", 45, "Zen School")
# student1.print_urschool()
# student1.print_urage()
# student1.print_urname()

# --------**其他測試自我補充**--------
# for in 迴圈 逐行列出list的資料
# listtest = []
# listtest.append(50)
# listtest.append(110)
# listtest.append(180)
# for i in range(3):
#     print(i,":",listtest[i])

# # os 的創見資料夾(測不出效果!)
# # os.path.join(dirpath, filename)	將 dirpath 與 filename 結合，無需自行判斷要用 '\\' 或 '/' 。
# # os.mkdir(path, mode=0o777, *, dir_fd=None)	建立 path 路徑，如果已存在就會發起例外。
# import os
# foldername = "cutedir"
# path01 = os.path.join(foldername)
# print("\n" + str(path01))
# save_as = os.path.join(path01,foldername + "001")
# print("\n" + str(save_as))
# os.mkdir(foldername)
