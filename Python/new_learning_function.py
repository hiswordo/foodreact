
# ---< 取得檔案創立時間 >---
import os
import datetime

#取得檔案修改時間，如果要用創立時間 用 os.path.getctime
unix_time = os.path.getmtime(file_path)
#轉時間物件
datetimeObj = datetime.datetime.fromtimestamp(unix_time)
#轉字串
dateStr = datetimeObj.strftime('%Y-%m-%d_%H%M%S')


