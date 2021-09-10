# 教學:https://www.youtube.com/watch?v=IbGJaTkyuXA&list=PLSCgthA1AnieCi1FfNibjYWkLWIPi92Yu&index=4
import eel
import random

eel.init('web')

# # 從調用js函數
# def print_js(x):
#     print(x)
# eel.hello()(print_js)  #後面()接收前面的回傳

# js調用python函數
# @eel.expose # 加速器??
# def ran_int():
#     return random.randint(0,100)

eel.start('main.html', size=(1000,800), position=(200,200))
# 預設是mode='chrome-app'

# 從js調用函數slo2. 測試中
# You can only perform synchronous returns after the browser window has started (after calling eel.start()), otherwise obviously the call will hang.
# x = eel.hello()()
# print(x)

# 若要等待時間
# time.slepp(5)是錯誤的
# eel.sleep(5) 就可以了

# 官文: https://github.com/ChrisKnott/Eel#app-options
# 建議: 不用VScode開啟，後台不會自動關閉