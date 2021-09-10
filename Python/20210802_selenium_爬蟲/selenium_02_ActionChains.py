# Action Chains 
# 教學 https://www.youtube.com/watch?v=ximjGyZ93YQ#t=28m58s
# 7.2 https://selenium-python.readthedocs.io/api.html

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:/chromeauto/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://tsj.tw/")

blow = driver.find_element_by_id("click")
blow_count = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]') #因為沒找到特徵，可以用xpath看看。發現雙引號在裡面，外面記得改單引號

#策略從貴的開始買 20,15,10(此價格會一直變動，他也會一直重抓)，目前的寫法，實際執行的效果一開始確實最貴先買，但後來會變成哪個買得起就買哪個
item = []
item.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))  #最貴的購物按鈕button
item.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
item.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))

item10 = []
item10.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[3]')) 
item10.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[3]')) 
item10.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[3]')) 

price = []
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]')) #第三層的價格td
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))

actions = ActionChains(driver) #創建action物件，傳入的參數為操作的瀏覽器driver
actions.click(blow) #直到perform才會開始執行，那順序狀況會是怎樣呢??

for i in range(10000):
    actions.perform()
    blow_count_int = int((blow_count.text.replace("您目前擁有","").replace("技術點",""))) #每次都會自動更新blow_count抓一次?? 這樣很厲害耶，會再執行的真實原因是甚麼阿??
    for j in range(3):
        price_int = int(price[j].text.replace("技術點",""))
        if blow_count_int >= price_int*10:  #10倍按鈕根本用不到...
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item10[j])  #移到這個位置，也可以不用，直接click(item10[j])就好
            upgrade_actions.click()
            upgrade_actions.perform()
            break  #因為這是跑三次比較，假設你是20>=20執行了，20>=15又執行，20>=10也執行，當然出問題，所以需要讓他離開迴圈，才不會技術點不夠還一直按購買
        elif blow_count_int >= price_int:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.click(item[j])
            upgrade_actions.perform()
            break  


# action.perform()