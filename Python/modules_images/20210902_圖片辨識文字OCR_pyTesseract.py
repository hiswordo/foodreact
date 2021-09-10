# ----Tesseract----
# @link [光學字符識別 Tesseract-OCR 的下載、安裝和基本用法 - 台部落](https://www.twblogs.net/a/5d52ab0ebd9eee5327fccbad) at 2021/9/1
""" 
1. 下載地址二：https://digi.bib.uni-mannheim.de/tesseract/ （僅Windows操作系統，歷史版本）
2. 可先選需要的就好，之後可以補，Additional language data(download) [under Tesseract-OCR\tessdata\tessconfigs]
3. 配置環境變量Path:Tesseract-OCR安裝路徑
4. 終端機檢驗是否安裝成功，tesseract -v
5. 基本用法
    完整命令：tesseract 圖片路徑和圖片名 結果路徑和結果名 -l 語言
    舉例：tesseract F:\code\test.png F:\code\result -l eng
    注意：
    1、需要識別的圖片要加後綴
    2、結果文件名不需要加後綴，會自動加後綴，生成的是txt文件
    3、-l 是英文字母l，不是數字1，language 語言的意思，不加默認英文
    4、eng 表示英文，chi_sim 表示簡體中文
    5、將cmd切換到要識別圖片的文件夾後，就不用加圖片路徑 
6. pip install pytesseract & Pillow
7. py的檔名不能是"pytesseract.py" 會跟裡面import衝突，產生 AttributeError: partially initialized module 'pytesseract' has no attribute 'image_to_string' (most likely due to a circular import)
"""
# 語言包名稱
# chi_sim
# chi_sim_vert
# chi_tra
# chi_tra_vert
# eng
# jpn
# jpn_vert
# osd

import pytesseract as pytess
from PIL import Image

# ----基本測試----
# 打開圖片
filename = r"\tradchin.PNG"
path = r"Python\modules_images\imgs"
print(path + filename)
img = Image.open(path + filename)
# 識別圖片
# ocrcontent = pytess.image_to_string(img, lang="eng")
# ocrcontent = pytess.image_to_string(img, lang="chi_tra")
# ocrcontent = pytess.image_to_string(img, lang="chi_sim")
# ocrcontent = pytess.image_to_string(img, lang="jpn")
# print(ocrcontent) # (錯誤:4個字)

# *測試結果: 基本上，只有eng可以跟其他語言互相混和，本身準確率也最高

# ----灰度化圖片後辨識OCR---
# @link [Tesseract OCR V5.0安裝教程（Windows） - 簡書](https://www.jianshu.com/p/f7cb0b3f337a) at 2021/9/2

# 建议图像识别前，先对图像进行灰度化和 二值化，以提高文本识别率
# image = Image.open(file)
Img = img.convert("L")  # 灰度化
# 自定义灰度界限，这里可以大于这个值为黑色，小于这个值为白色。threshold可根据实际情况进行调整(最大可为255)。
threshold = 165  # 由白到黑 120 左右
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
photo = Img.point(table, "1")  # 图片二值化
# 保存处理好的图片
photo.save(path + r"\tradchin_new.PNG")

img = Image.open(path + r"\tradchin_new.PNG")
# 解析图片，lang='chi_sim'表示识别简体中文，默认为English
# 如果是只识别数字，可再加上参数config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
ocrcontent = pytess.image_to_string(img, lang="chi_tra", config="--psm 6")
print(ocrcontent)

# *測試對象: tradchin.PNG (直接截圖文字的圖片)
# *測試結果:
""" 
threshold = 120 確實比較接近原圖灰度化
以預設"--psm 3"來執行 : 85 較好 (錯誤:2個字，但未辨識達10幾個字)，更差了
- 3：Fully automatic page segmentation, but no OSD. (Default)
但當灰度化 > 100 後，模式3，幾乎抓不到字
改以"--psm 6"來執行 : 165 較好 (準確度來到100%)，這樣就有差別了
- 6：Assume a single uniform block of text. 
 """

# open cv
# @link [使用 OpenCV 及 Tesseract 進行 OCR 辨識(3)-使用 Tesseract 進行 OCR 辨識 | by AndyLin | Pivot the Life | Medium](https://medium.com/pivot-the-life/%E4%BD%BF%E7%94%A8-opencv-%E5%8F%8A-tesseract-%E9%80%B2%E8%A1%8C-ocr-%E8%BE%A8%E8%AD%98-3-%E4%BD%BF%E7%94%A8-tesseract-%E9%80%B2%E8%A1%8C-ocr-%E8%BE%A8%E8%AD%98-e5e5abcecd97) at 2021/9/2


# 補充
# @link [在Python中打开Image.open之后是否不必关闭？ | 码农家园](https://www.codenong.com/968ea45ad411d0e702e6/) at 2021/9/1
# @link [真實場景下的Tesseract4.0神經網路訓練識別圖片驗證碼_州的先生 - MdEditor](https://www.gushiciku.cn/pl/pCrr/zh-tw) at 2021/9/2
# @link [了解圖片內容 - iT 邦幫忙一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10233380) at 2021/9/2