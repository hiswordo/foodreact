# 教學:https://www.youtube.com/watch?v=7IFhsbfby9s
# https://zhuanlan.zhihu.com/p/192747600
import cv2
# import numpy as np
# from cv2 import CascadeClassifier
# from matplotlib import pyplot as plt

def facepic(image):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Read the input image
    img = cv2.imread(image)

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces # 導致終端機不停...
    faces = face_cascade.detectMultiScale(gray, 1.2, 3) #(gray,scaleFactor=1.2,minNeighbors=3,) 1.1, 4
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print('x:',x,'y:',y,'wide:',w,'height:',h)

    # # Display the output RGB格式。2nd way
    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.title('my picture')
    # plt.show()

    # # Display the output 是BGR格式
    # cv2.imshow('img', img)
    cv2.imwrite('new'+image, img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imshow('img', img)
    # while cv2.waitKey(100) != 27:# loop if not get ESC
    #     if cv2.getWindowProperty('img',cv2.WND_PROP_VISIBLE) <= 0:
    #         break
    # cv2.destroyWindow('img')

    # 這是for videos的吧
    # cv2.imshow('img', img)
    # k = cv2.waitKey(0) # waitkey代表读取键盘的输入，括号里的数字代表等待多长时间，单位ms。 0代表一直等待
    # if k ==27:     # 键盘上Esc键的键值
    #     cv2.destroyAllWindows() 
facepic(f"test1.jpg")

# for i in range(1,6):
#     facepic(f"test ({i}).jpg")