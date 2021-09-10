import os
# @link [【Python】取出檔案名稱 (含副檔名、不含副檔名) os path basename split 取出 檔名 路徑 不要副檔名 (內含範例程式碼) sample code - 嗡嗡的隨手筆記](https://www.wongwonggoods.com/python/python_file_process/os-path-basename-split/) at 2021/9/3
# filepath = "/home/ubuntu/python/example.py"
# basename = os.path.basename(filepath)  # basename - example.py
# filename = os.path.splitext(basename)[0]  # filename - example

# ----切割: 最基本的 split----
filepath =  '/home/ubuntu/python/example.py'
result = filepath.split('/') 
print(result) # ['', 'home', 'ubuntu', 'python', 'example.py']
print(result[-1])

# ----切割: 路徑 + 檔名.副檔名----
filepath = '/home/ubuntu/python/example.py'
result = os.path.split(filepath)
print(result) # ('/home/ubuntu/python', 'example.py')

# ----切割 "檔名"----
filename = os.path.splitext('exam.ple.py')[0] # ('exam.ple', '.py')
print(filename) #exam.ple
# OR
filename = 'exam.ple.py'.split(".")[0] # 此作法風險：檔案名稱內有其他".""
print(filename)

# ---- 直接讀: "檔名.副檔名" basename ----
import os
filepath = '/home/ubuntu/python/example.py'
basename = os.path.basename(filepath) # example.py
print(basename)