
# 2021.08.14
# Jupyter某檔案上半頁面消失，結果"重新命名"檔案就出來了...


# 2021.08.06
# # 001:windows非法字元 \ / : * ? " < > | 處理
# import re
# originalName = "/ラブホドキュメンタリー休憩2時間/3"
# fileName = re.sub('[\/:*?"<>|]','',originalName) #去掉非法字元，可以編輯self來做更多操作
# print(fileName)

# # 002:字數過多的處理
# wordtest = "NTK-613 【ピーカン！！美少女3人！！全員清純系ビッチ！！大乱交“6P”スペシャル！！】まさに酒池肉林！！美少女×3人！！全員ド淫乱ドビッチという奇跡の3性豪が晴天の下に集結でお祭り騒ぎ！！長身スレンダーで美脚でビンカン美乳という奇跡の美少女が…夏の太陽の下で大乱れ連続生チン挿入&中出し！！/男優のセフレ/ヤリサーSP"
# 002.1:逐步刪減空白後面的文字
# wordtest = "make love and east side"
# newword = wordtest.rindex(" ")
# manytime = wordtest.find(" ")
# manytime = wordtest.count
# print(len(wordtest))
# print(manytime)
# nextword = wordtest
# for i in range(manytime):
#     if len(nextword) > 13 : #13的位置剛好在and結尾，則最終型態會保留在13
#         print("刪減第"+str(i)+"次:"+nextword)
#         spacePos = nextword.rindex(" ")
#         nextword = wordtest[0:spacePos]
# print("最終型態"+nextword)    
    
# 002.2:逐步判斷空格位置
# wordtest = "make love and east side"
# spacePos = []
# lenSentence = 13
# lengthWordtest = len(wordtest)
# for i in range(lengthWordtest):
#     if wordtest[i]==" ":
#         spacePos.append(i)
# for j in spacePos:
#     if j > lenSentence-1:
#         finalWord = wordtest[0:j]
#         break
# print(finalWord)

# XXX 002.2:逐步判斷空格與不同符號的位置，並刪減程式和字數
# wordtest = "knowledge love and… east side！"
'''
def shrinkSenten(wordtest,num):#(文字，需要小於字串長度)
    lenSentence = num
    syntaxPos = []
    syntaxWd = [' ','！','…','】']
    for i in range(len(wordtest)):
        for k in syntaxWd:
            if wordtest[i]==k:
                syntaxPos.append(i)
                break
    # print(syntaxPos)
    syntaxPos.reverse() #從最後的符號跑到最前面
    for j in syntaxPos:
        if j < lenSentence-1: 
            if wordtest[j]==" ":
                finalWord = wordtest[0:j] #最終字串，刪除空白
                return finalWord
            else:
                finalWord = wordtest[0:j+1] #最終字串，保留符號本身
                return finalWord
    # print(finalWord)
'''

# # input接著顯示
# value = input("Hi give me a number? I'll add 6 to it.\n")
# value = value+6
# print('the outcome will be ', value)
# @learn Python F-strings 字串格式化 formatted string literals又稱Literal String Interpolation（字串插值）after python3.6
# # 引用的方式 {} 這樣好寫很多耶! f表format格式化字串，內部可以放變數、表示式、函式
# value1 = input("Please enter a string by number:\n")
# print(f'You entered {value1} and its type is {type(value1)}')
# value2 = int(input("Please enter an integer:\n"))
# print(f'You entered {value2} and its type is {type(value2)}')
# print(f'And you know value1 + value2 = {int(value1)+value2} ')
# #文字本身及表示式結果，緊接著出來，加個等於就可以了
# x,y = 1,2
# print(f'{x + y = }')  # x + y = 3
# print(f'{x > y = }')  # False
# l,z = 'text',' test'
# print(f'{l + z =} ') # l + z ='text test'
# l,z = 'text', 5
# print(f'{l, z =} ') # l, z =('text', 'test')
# print(f'{[l,z] =} ')

# 檔名過濾
# import re
# from sys import flags
# # testword = "fc2-ppv 1456822"
# testword = "You Can Ejaculate One More Time, IPX-671Right Hikari Azusa + Slut Awakening + Ultimate"
# print(re.findall('fc2',testword,re.I))
# if re.findall('fc2',testword,re.I)!=[]:
    # print(re.search(r'fc2-?[a-z0-9]{0,}(-|\s)[0-9]{2,}',testword,re.I)[0])
#     print("fc2")
# else:
#     nexting = re.search(r'[a-z][a-z0-9]{0,}-[0-9]{2,}',testword,re.I)[0]
#     print(nexting)

# # 中文資訊
# https://javpapa.com/?s=IPX-480
# https://www.444.coffee/?post_type=post&s=IPX-480%EF%BB%BF
# https://avbebe.com/archives/63715