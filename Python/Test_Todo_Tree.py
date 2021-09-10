# ---- title ----
# @link [GitHub - Gruntfuggly/todo-tree: Use ripgrep to find TODO tags and display the results in a tree view](https://github.com/Gruntfuggly/todo-tree#highlighting) at 2021/9/6
# TODO：知道要實作什麼功能，但還沒開始寫的程式碼。

# FIXME stime went wrong
""" a = 1 + b = 5 """

# FIXME: stime went wrong
# a = 1 + b = 5

# ---- Fixed ----
# FIXED: 已修復
""" a = 1 + b = 5 """

# FIXED: 已修復
# a = 1 + b = 5

# XXX：很醜程式碼，有空再優化。
a = 1
b = 2
print(a+b) # ?? 真的很醜

# BUG: 類似FIXME?


# Hi hello # REVIEW[0]: test


# icon選擇
# @link [Octicons](https://primer.style/octicons/) at 2021/9/6
# @link [codicon | The icon font for Visual Studio Code](https://microsoft.github.io/vscode-codicons/dist/codicon.html) at 2021/9/6

""" 
"type":
tag - 預設
text - tag + 之後
tag-and-comment - 註解標籤 + tag
tag-and-subTag - 未知
text-and-comment - 註解標籤 + tag + 之後
line - 整行字
whole-line - 整行字 + 螢幕寬度
"""