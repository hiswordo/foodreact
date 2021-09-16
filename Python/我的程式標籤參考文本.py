----大標題----
""" 
# Better Comment: 大小寫不分，無法即時更新顏色
# - print("內容")
# Todo-Tree: 大小寫敏感，可以即時更新顏色
"""
# ---< 小標 >---
print("內容")
print("不懂內容") # ?? 不懂內容
print("內容")
print("內容")
print("內容")
print("內容")


# ---[ 類型: 工具名 ]---
print("內容")
print("內容error") # FIXME
print("內容")
print("內容")

# TODO: 未完成目標

# REVIEW
print("內容")
print("內容")
print("內容")
# XXX 不良程式/不懂的程式/
print("....")
print("....")



# XLX: 原本的錯誤紀錄
# CLR: 完成?
# @link...
# // 犯錯紀錄?
# ! 注意事項

# "BUG",
# "HACK",

# @link [[學習筆記] 如何撰好的 Git Commit Message | 前端新米](https://heidiliu2020.github.io/git-commit-message/) at 2021/9/16
# Git Commit Message 的規範與準則
# 一個 Commit Message 主要由 Header + Body + Footer 組成：

# <type>(<scope>): <subject>
# 
# <body>
# 
# <footer>

# Commit Message 範例
""" 
feat: message 新增信件通知功能
feat(優惠券): 加入搜尋按鈕，調整畫面

fix: 圓餅圖圖例跑版
fix: 意見反應，信件看不到圖片問題

style: 統一換行符號 CRLF to LF

docs: 更新 README 相關資訊
docs: 修正型別註解

chore(submoudle): 變更 git url
chore: 調整單元測試環境

refactor(每日通知信件): 重構程式結構 
"""

# type 使用慣例：
""" 
feat：新增或修改功能（feature）
fix：修補 bug（bug fix）
docs：文件（documentation）
style：格式
    不影響程式碼運行的變動，例如：white-space, formatting, missing semi colons
refactor：重構
    不是新增功能，也非修補 bug 的程式碼變動
perf：改善效能（improves performance）
test：增加測試（when adding missing tests）
chore：maintain
    不影響程式碼運行，建構程序或輔助工具的變動，例如修改 config、Grunt Task 任務管理工具
revert：撤銷回覆先前的 commit
    例如：revert：type(scope):subject 
merge：代码合并。
sync：同步主线或分支的Bug。

data: 相關資料存檔 (不知道的檔案居多)
res: 相關資源存檔 (知道的圖檔、音檔等)
try: 純測試新功能檔案 (之前都存成test了...)
"""

# Header
# type（必要）：如：feat, fix, docs, style, refactor, test, chore
# scope（可選）：如：資料庫、控制層、模板層等，視專案不同改變
#   如果你的修改影响了不止一个scope，你可以使用*代替。
# subject（必要）：commit 的簡短描述
# 不超過 50 個字元
# 結尾不加句號
# 盡量讓 Commit 單一化，一次只更動一個主題

# Body
# 對本次 Commit 的詳細描述，解釋 What & Why & How
# 可以分成多行，每一行不超過 72 個字元
# 說明程式碼變動的項目與原因，還有與先前行為的對比

# Message Footer
# 填寫任務編號 issue #1246 (需求链接状态变化 (Closes #392))
# BREAKING CHANGE（可略），記錄不兼容的變動，後面是對變動的描述、以及變動原因和遷移方法

# @link [Git commit message格式规范（推荐） - 簡書](https://www.jianshu.com/p/e749ec630556) at 2021/9/16
# Examples :
""" 
feat($browser): onUrlChange event (popstate/hashchange/polling)

Added new event to $browser:
- forward popstate event if available
- forward hashchange event if popstate not available
- do polling when neither popstate nor hashchange available

Closes #1213242
"""
# Examples :
"""
fix($compile): couple of unit tests for IE9

Older IEs serialize html uppercased, but IE9 does not...
Would be better to expect case insensitive, unfortunately jasmine does
not allow to user regexps for throw expectations.

Closes #17116
"""