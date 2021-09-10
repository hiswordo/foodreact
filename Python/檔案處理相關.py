

# 檔案讀取 # 此相對路徑不是py的位置，是vscode的工作區域
filename = "testing.txt"
with open("testing.txt", mode="r", encoding="utf-8") as f:
    # f.seek(0) # 如果是空的，可以考慮讓記得讓游標移到最開始
    content_list = f.read()