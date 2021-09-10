# Selenium 網頁自動化
# 教學 https://www.youtube.com/watch?v=ximjGyZ93YQ

#取得網頁標籤 & 常用網頁操作
from selenium import webdriver
# 搜尋欄需要輸入文字
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys #需要用到鍵盤的時候，注意Keys大寫
# Explicit Waits使用
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 等待時間使用
import time

PATH = "C:/chromeauto/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# 開啟、title抓取、關閉網頁
# driver.get("https://google.com")
# print(driver.title)
# driver.quit() # driver.close() 

driver.get("https://www.dcard.tw/f")
# 搜尋欄輸入搜尋關鍵字
search = driver.find_element_by_name("query")
search.clear() #清空輸入欄位，避免搜尋欄位本身有東西
search.send_keys("比特幣")
search.send_keys(Keys.RETURN) #RETURN就是ENTER鍵  #重要提示! 頁面跳轉需要時間的! 
# time.sleep(3) #可以用但不是好辦法
# 使用Explicit Waits https://selenium-python.readthedocs.io/waits.html
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1")) #為什麼By.可以跳出那些ID選項?? 代碼提示??
    ) #等待時間上限10秒，等待網頁讀出看板 (class name:sc-3yr054-1的element後再執行下方程式碼)

# 抓取每項小標題
# titles = driver.find_elements_by_class_name("tgn9uw-3") #elements才會找多個，不然只找第一個
# for title in titles:
#      print(title.text) #.text直接取得裡面文字

# 點擊開啟連結
link = driver.find_element_by_link_text("老二以太坊再度發威領漲，主流幣、價值幣、平台幣補漲！") #一個字不對就無法了?? 如果其中有字做em改變class也無法讀取到??
link.click()
driver.back() #上一頁
driver.back()
driver.forward() #下一頁


time.sleep(5)
driver.quit()