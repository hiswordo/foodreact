# 教學1:https://www.youtube.com/watch?v=i_rMqj-bm44
# 教學2:https://www.youtube.com/watch?v=l1MAW1z641E
# 教學2文本:https://github.com/MorvanZhou/tutorials/blob/master/basic/36_regex.ipynb
# 教學2網站:https://mofanpy.com/tutorials/python-basic/basic/regular-expression/
# 工具:https://regexr-cn.com/
# 課程:https://codejiaonang.com/#/course/regex_chapter1/0/0
# 官方文本:https://docs.python.org/zh-tw/3.5/library/re.html

# 表達式: 
    # ^非，|或，{3:4}3到4次，貪婪4次，{3:4}?非貪，*0次以上={0,}，+1次以上={1,}，.表達任何字
    # 0=[0]，/d=[/d]，單一位，可能出現的集合意思
    # \d 數字decimal digit，\w 所有字母数字和"_" (大寫則為非)，特殊字符\\，\. (取消原本\跟.的意思)
    # 中文:[\u4e00-\u9fa5]，網址:[a-zA-z]+://[^\s]* (因為網址不會有空白阿) 我的寫法:h[a-zA-Z]+://\S+
# re: split()分割，sub()替換，compile()表達式暫存?
import re
# string1 = "a dog runs to a cat, a black Dog and another whitle dogs"
# pattern1 = "dog"
# # python本身好用的邏輯!
# print(pattern1 in string1) #True
# pattern2 = "cats"
# print(pattern2 in string1) #false
# # 表達式
# ptn = r"r[au]n" # 加了r變成表達式可以用[]等
# print(re.search(ptn,string1)) # <re.Match object; span=(6, 9), match='run'> # 全字串第一個，就一個
# print(re.search(ptn,string1)[0]) # run # 所以只有[0]
# ptn = r"dogs?"
# print(re.findall(ptn,string1)) # ['dog', 'dogs'] # 全字串的每一個，可以分別丟出來
# print(re.findall(ptn,string1,flags=re.I)) # I=ignore大小寫 # flags=可省略
# print(re.match(ptn,string1)) # None # match只會找開頭，string1"dog want"就會找到

# 空白
# \s : any white space [\t\n\r\f\v]
# print(re.search(r"r\sn", "r\nn r4n"))               
# # \S : opposite to \s, any non-white space
# print(re.search(r"r\Sn", "r\nn r4n"))

# 空白字符
# # \b : empty string (only at the start or end of the word)
# print(re.search(r"\bruns\b", "dog runs to cat"))    
# # \B : empty string (but not at the start or end of a word)
# print(re.search(r"\B runs \B", "dog   runs  to cat"))

# print(re.search(r"r.n", "r[ns to me")) # . : match anything (except \n)
# print(re.search(r"Mon(day)?", "Monday"))      
# print(re.search(r"Mon(day)?", "Mon"))

# 多行匹配 multi-line
# string = """
# dog runs to cat.
# I run to dog.
# """                
# print(re.search(r"^I", string, flags=re.MULTILINE)) # M = MULTILINE

# group #若太多組，會分不清楚group(?)表達的東西
# match = re.search(r"ID: (\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
# print(match.group()) # ID: 021523, Date: Feb/12/2017                               
# print(match.group(1)) # 021523                             
# print(match.group(2)) # Feb/12/2017
# 將group命名ID，?P<ID>
# match = re.search(r"ID: (?P<ID>\d+), Date: (?P<Date>.+)", "ID: 021523, Date: Feb/12/2017")
# print(match.group()) # ID: 021523, Date: Feb/12/2017                               
# print(match.group('ID')) # 021523                             
# print(match.group('Date')) # Feb/12/2017

# 找開頭，與找結尾
# stringTest = "python 1234 python"
# restring = re.search('^python',stringTest)
# print(restring)
# restring = re.search('python$',stringTest)
# print(restring)
