# 
# @link [針對複雜場景的 OCR 文字識別，推薦一個Python 庫！_zeroing1 - MdEditor](https://www.gushiciku.cn/pl/g8Zy/zh-tw) at 2021/9/13
# @link [Optical Character Recognition with EasyOCR and Python | OCR PyTorch - YouTube](https://www.youtube.com/watch?v=ZVKaWPW9oQY) at 2021/9/13
import easyocr
import streamlit as st  # Web App
from PIL import Image, ImageDraw  # Image Processing
import numpy as np  # Image Processing

# easyocr 將所有功能都封裝到一個類中 Reader ，可通過呼叫類裡面的三種方法 readtext、detect、recognize 來實現，

# 預設: gpu=True
reader = easyocr.Reader(["en"], gpu=False, model_storage_directory="./model")
# reader = easyocr.Reader(["ch_sim", "en"], gpu=False, model_storage_directory="./model")
# *使用執行命令: $ easyocr -l ch_sim en -f XX.jpg --detail=1 --gpu=True  

# ---< detect method >---
# *Method for detecting text boxes.
# detect 方法用於檢測影象中的文字框，最終返回兩個列表，來表示文字框在影象中的位置，一個為 horizontal_list 格式為 [x_min,x_max,y_min,y_max] ，另一個為 free_list ，格式為 [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]，
resultDet = reader.detect("./modules_images/imgs/eng.jpg")
print(f'{resultDet = }')
# ([[[118, 256, 10, 38], [93, 281, 41, 81], [30, 344, 68, 116], [85, 283, 109, 149], [127, 247, 157, 171], [130, 242, 509, 523], [245, 271, 511, 523]]], [[]])


# ---< recognize method >---
# *Method for recognizing characters from text boxes. If horizontal_list and free_list are not given. It will treat the whole image as one text box.
# recognize 用於識別，使用該函式時需要提供三個引數，image、horizontal_list、free_list，使用時與 detect 相搭配
resultRecAll = reader.recognize("./modules_images/imgs/eng.jpg")
print(f'{resultRecAll = }')
# [([[0, 0], [375, 0], [375, 521], [0, 521]], '6', 0.4073288163001507)] 整張圖的回傳結果，整張圖的樣子，對應中文字的話好像蠻酷的
# 輸入list，少數很難定義的字範圍才會需要用到手動調整
""" resultRec = reader.recognize("./modules_images/imgs/eng.jpg", horizontal_list=[[118, 256, 10, 38], [93, 281, 41, 81], [30, 344, 68, 116], [85, 283, 109, 149], [127, 247, 157, 171], [130, 242, 509, 523], [245, 271, 511, 523]], free_list=[]) 
# TypeError: 'NoneType' object is not iterable or TypeError: '>' not supported between instances of 'list' and 'int'
print(f'{resultRec = }')
# [([[118, 10], [256, 10], [256, 38], [118, 38]], 'Karl Fulves', 0.7241827736168135), ([[93, 41], [281, 41], [281, 81], [93, 81]], 'Easy-to-Do', 0.8780171714108821), ([[30, 68], [344, 68], [344, 116], [30, 116]], 'MAGIC TRICKS', 0.9998409251539293), ([[85, 109], [283, 109], [283, 149], [85, 149]], 'for Children', 0.9999525871741958), ([[127, 157], [247, 157], [247, 171], [127, 171]], 'Wlth 63 Illustrations', 0.8355009505982067), ([[130, 509], [242, 509], [242, 521], [130, 521]], 'DoverPublications', 0.9952612644354866), ([[245, 511], [271, 511], [271, 521], [245, 521]], 'com', 0.4681754712664712)] """

# ---< detect method : Method for detecting text boxes. >---
# readtext 函式是將 detect 和 recognize 方法相結合：先利用 detect 函式識別影象中文字框的位置座標，將座標列表輸入 recognize 進行識別，最終返回每個文字資訊及位置座標
# return 左上、右上、右下、左下 , '字', 信心
resultRead = reader.readtext("./modules_images/imgs/eng.jpg")
# [([[118, 10], [256, 10], [256, 38], [118, 38]], 'Karl Fulves', 0.7241827736168135), ([[93, 41], [281, 41], [281, 81], [93, 81]], 'Easy-to-Do', 0.8780171714108821), ([[30, 68], [344, 68], [344, 116], [30, 116]], 'MAGIC TRICKS', 0.9998409251539293), ([[85, 109], [283, 109], [283, 149], [85, 149]], 'for Children', 0.9999525871741958), ([[127, 157], [247, 157], [247, 171], [127, 171]], 'Wlth 63 Illustrations', 0.8355009505982067), ([[130, 509], [242, 509], [242, 521], [130, 521]], 'DoverPublications', 0.9952612644354866), ([[245, 511], [271, 511], [271, 521], [245, 521]], 'com', 0.4681754712664712)]
resultRead0 = reader.readtext("./modules_images/imgs/eng.jpg", detail = 0)
# ['Karl Fulves', 'Easy-to-Do', 'MAGIC TRICKS', 'for Children', 'Wlth 63 Illustrations', 'DoverPublications', 'com']
print(f'{resultRead = }')
print(f'{resultRead0 = }')


# 幫字打上紅框框
img = Image.open("./modules_images/imgs/eng.jpg")
draw = ImageDraw.Draw(img)

for i in resultRead:
    draw.rectangle((tuple(i[0][0]),tuple(i[0][2])),fill=None,outline='red',width=2)
img.save("./modules_images/imgs/eng_easyocr.jpg")


# @link [EasyOCR | Extracting Text From Image using EasyOCR](https://www.analyticsvidhya.com/blog/2021/06/text-detection-from-images-using-easyocr-hands-on-guide/) at 2021/9/13