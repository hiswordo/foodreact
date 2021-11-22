
# @link [推薦一款最強Python自動化神器！不用寫一行程式碼！ | IT人](https://iter01.com/571557.html) at 2021/9/28
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright, fillword) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.foodpanda.com.tw/login/new?step=email
    page.goto("https://www.foodpanda.com.tw/login/new?step=email")

    # Click [data-testid="email-view-text-field"]
    # page.click("[data-testid=\"email-view-text-field\"]")


    # Fill [data-testid="email-view-text-field"]
    page.fill("[data-testid=\"email-view-text-field\"]", "cokehour"+fillword+"y7@gmail.com")
    print(fillword)

    # Press Enter
    # with page.expect_navigation(url="https://www.foodpanda.com.tw/login/new?step=registration"):
    with page.expect_navigation(url="https://www.foodpanda.com.tw/login/new?step=registration"):
        page.press("[data-testid=\"email-view-text-field\"]", "Enter")

    # Click [data-testid="email-view-continue-button"]
    # with page.expect_navigation(url="https://www.foodpanda.com.tw/login/new?step=registration"):
    # with page.expect_navigation():
    #     page.click("[data-testid=\"email-view-continue-button\"]")

    # ---------------------
    context.close()
    browser.close()

# cokehourtoy7@... 
# xo連續試成功了喔~
englist =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'o', 'p', 'r', 's', 't', 'u']
finallist=[]
for x in englist:
    y = 'o'
    finallist.append(x+y)
finallist
# testlist = ["mo","ko"]

for fillword in finallist:
    with sync_playwright() as playwright:
        run(playwright, fillword)






# %%
# englist = [chr(w) for w in range(ord('a'), ord('z') + 1)]
# englist.remove("q")
# englist.remove("z")
# englist.remove("x")
# englist.remove("v")
# englist.remove("w")
# englist.remove("n")
# englist.remove("m")
# englist.remove("y")
# englist
# %%
# englist =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'o', 'p', 'r', 's', 't', 'u']
# finallist=[]
# for x in englist:
#     for y in englist:
#         finallist.append(x+y)
# finallist
# %%
