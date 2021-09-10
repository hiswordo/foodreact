# ig圖片下載

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
# 下載圖片與創建資料夾需要引入
import os
import wget

PATH = "C:/chromeauto/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
# 等ig讀取差不多
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

# 連線到fb並登入
linkfb = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button')
linkfb.click()

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email")) #等待同時能獲得哪些資訊阿?? 還可以直接拿來sendkey
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "pass"))
)

username.clear()
password.clear()
username.send_keys("")
password.send_keys("")
login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
login.click()

# 回到ig，搜尋圖片 (fb回ig可以很久)
nexttime = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))
) # driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
nexttime.click() # 點擊:稍後再說

searchbar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)

# 兩次enter才能搜尋成功
keyword = "#cat"
searchbar.send_keys(keyword)
time.sleep(1)
searchbar.send_keys(Keys.RETURN)
time.sleep(1)
searchbar.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_7A2D8")) #等搜尋結果出來
)

# 滑到最底部，讀取更多圖片
# for i in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)

# 創建資料夾並下載到裡面
# path = os.path.join(keyword) # 不懂有啥意義?? 目前測試沒有任何新增效果
os.mkdir(keyword) # path->keyword

imgs = driver.find_elements_by_class_name("FFVAD")
count = 1
for img in imgs[0:2]:  # 下載圖片數量，[0:2]表示[0][1]兩張圖片
    # save_as = keyword + str(count) + ".jpg"
    save_as = os.path.join(keyword, keyword + str(count) + '.jpg') # 相對路徑合併 #cat/#cat1.jpg 目前理解?? #save_as得到#cat\#cat1.jpg
    # print(img.get_attribute("src")) #抓出圖片位置
    # print(img.get_attribute("src"))
    # print(save_as)
    wget.download(img.get_attribute("src"),save_as)
    count += 1
