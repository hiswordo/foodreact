# 原先bs4做法完全不行
# from modules.crawler import pageParser

from modules.crawler import jsonParser
import html

# 網址的選取按F12 打開開發者工具 > Network > XHR。重新整理。
url = "https://www.google.com/maps/vt?pb=!1m4!1m3!1i15!2i27444!3i14022!1m4!1m3!1i15!2i27444!3i14023!1m4!1m3!1i15!2i27445!3i14022!1m4!1m3!1i15!2i27445!3i14023!1m4!1m3!1i15!2i27446!3i14022!1m4!1m3!1i15!2i27446!3i14023!1m4!1m3!1i15!2i27444!3i14024!1m4!1m3!1i15!2i27444!3i14025!1m4!1m3!1i15!2i27445!3i14024!1m4!1m3!1i15!2i27445!3i14025!1m4!1m3!1i15!2i27446!3i14024!1m4!1m3!1i15!2i27446!3i14025!2m3!1e0!2sm!3i567293864!2m48!1e2!2sspotlight-no-personal!5i1!8m44!11e7!12m40!3m1!3s0x3442aff29ae40df9%3A0x2196f568e76dfa81!3m1!3s0x3442ae8d02c2a24d%3A0x68fa12c3a19d5212!3m1!3s0x3442aeed008dc33f%3A0x6f92f5e8664539b5!3m1!3s0x3442ae900f56ece7%3A0x3a0b96c1db07b3cd!3m1!3s0x3442ae86f589eecd%3A0xfb35f872a34f5a0a!3m1!3s0x3442ae9768aeb189%3A0x411a14b07a03eb75!3m1!3s0x3442ae8c879d6aa3%3A0xe4c9b1e020b18109!3m1!3s0x3442ae9aef8c44a1%3A0x44da4e1d95fe3814!3m1!3s0x3442af769d7ab231%3A0xd2190004df05aa3e!3m1!3s0x3442ae9290fa98f9%3A0x804daddbf0cc9cec!3m1!3s0x3442ae855e20dfeb%3A0x389d2a11f6ea591f!3m1!3s0x3442ae877e957415%3A0x3d826362c1608df8!3m1!3s0x3442ae9a7a27de1d%3A0xf020841fe7cd0985!3m1!3s0x3442ae80c5641df7%3A0xe65c1876757c3edf!3m1!3s0x3442ae92902496b1%3A0x885dd27da1fe2bc4!3m1!3s0x3442afa7455f8a25%3A0xff3b290ee6216bb4!3m1!3s0x3442ae8793eff883%3A0x31d927f111352e1c!3m1!3s0x3442ae9b49e279ff%3A0xbcf4efefca1d80d8!3m1!3s0x3442ae9b3a7190f7%3A0xb81575d9e18c6c3c!3m1!3s0x3442ae845a3a5d4f%3A0x124c82731e5bd19b!20m1!1e4!3m12!2szh-Hant-TW!3sUS!5e78!12m4!1e68!2m2!1sset!2sRoadmap!12m3!1e37!2m1!1ssmartmaps!4e3!12m1!5b1&client=google-maps-lite&token=74651"
soup = jsonParser(url)
# print(type(soup)) #list

conlist = soup[1]
# c之後，還有"{\"1\":{\"title\":\"臺北市兒童新樂園(請至官網預約入園)\"}}"意思是{'1':{title:XXX}}，並小心"1"是字串
# {"1":{"title":"&#33274;&#21271;&#24066;&#20818;&#31461;&#26032;&#27138;&#22290;(&#35531;&#33267;&#23448;&#32178;&#38928;&#32004;&#20837;&#22290;)"}}
# print(conlist["features"][0]["c"])
# print(len(conlist["features"])) # 4 正確數量 # 字典數量

""" 什麼時候用 encode()、什麼時候用 decode()?
將 big5、utf-8 等碼轉成 Unicode 的動作（將外面的中文字串轉成 Python 內部的
Unicode 字串）時，則呼叫 decode()函數，反向的動作，則呼叫 encode()函數。 
tips：
str -> 通過encode（）-> 指定的bytes。 反過來，當從網路或磁碟上讀取了位元組流，讀到的數據就是bytes
bytes -> decode（）方法 -> str
編碼就是encode，把你認識的轉為，機器人認識
的 解碼decode，就是吧一堆機器認識的，解釋為人能讀懂的
"""
# &#33274;&#21271;&#24066;&#20818;&#31461;&#26032;&#27138;&#22290;(&#35531;&#33267;&#23448;&#32178;&#38928;&#32004;&#20837;&#22290;)
print(eval(conlist["features"][0]["c"])["1"]["title"]) # eval讓字串轉回表達式: 剛好適合{}這樣的字串
# print(eval(conlist["features"][0]["c"])["1"]["title"].encode("utf-8").decode("utf-8")) # 因為是str字串不會有任何效果...
print(html.unescape(eval(conlist["features"][0]["c"])["1"]["title"])) # 成功拉!
# print(html.unescape(a))
# ! python3以上取消了decode，所以你直接想st.decode（"utf-8"）的話會報str沒有decode方法的錯，所以需要先en在de
# !
""" 爬蟲時經常遇到'/u'開頭的unicode編碼的字元串，這時通過decode（）來解決.
但偶爾也會遇到以『&#』 或者『&#x』開頭的字串， 這是HTML、XML 等 SGML 類語言的轉義序列（escape sequence）。 它們不是「編碼」。
如果以『&#』 開頭，後接十進位數位，
如果以『&#x』開頭，後接十六進位數位。 """





# @link [Python 爬取Google map最新商家資訊評論!- 實作"動態網頁"爬蟲 | by zino lin | 誤闖數據叢林的商管人Zino | Medium](https://medium.com/%E8%AA%A4%E9%97%96%E6%95%B8%E6%93%9A%E5%8F%A2%E6%9E%97%E7%9A%84%E5%95%86%E7%AE%A1%E4%BA%BAzino/python-%E7%88%AC%E5%8F%96google-map%E6%9C%80%E6%96%B0%E5%95%86%E5%AE%B6%E8%B3%87%E8%A8%8A%E8%A9%95%E8%AB%96-%E5%AF%A6%E4%BD%9C-%E5%8B%95%E6%85%8B%E7%B6%B2%E9%A0%81-%E7%88%AC%E8%9F%B2-527d66a7e747) at 2021/8/16
# ----範例----
# # 超連結
# url = 'https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758546651144975!2y6093113884180453713!2m2!1i0!2i10!3e2!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sdzvaXrvAMImImAXHsLPICA!7e81'
# # 發送get請求
# text = requests.get(url).text
# # 取代掉特殊字元，這個字元是為了資訊安全而設定的喔。
# pretext = ')]}\''
# text = text.replace(pretext,'')
# # 把字串讀取成json
# soup = json.loads(text)

# # 取出包含留言的List 。
# conlist = soup[2]

# # 逐筆抓出
# for i in conlist:
#     print("username:"+str(i[0][1]))
#     print("time:"+str(i[1]))
#     print("comment:"+str(i[3]))
