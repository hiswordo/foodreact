from nltk.corpus import stopwords # nltk.download('stopwords')
from nltk.tokenize import word_tokenize  # 需要另外下載punkt.zip，解壓縮放到nltk_data底下
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer  # wordnet.zip
from nltk.probability import FreqDist
# import nltk
# from nltk import word_tokenize, pos_tag
from nltk import pos_tag  # nltk.download('averaged_perceptron_tagger')


# *獲取單字詞性的第一個字，並過濾掉只剩n,v,a,r
def get_wordnet_pos(tag):
    if tag[0] == "A":
        return "a"  #! pos=小寫英文
    elif tag[0] == "V":
        return "v"
    elif tag[0] == "N":
        if tag == 'NNP':
            return 'NNP'
        else:
            return "n"
    elif tag[0] == "R":  # 應該是副詞
        return "r"
    else:
        return None

# *讀取電影字幕檔案txt檔
filename = "testing.txt"
with open(filename, mode="r", encoding="utf-8") as f:
    # f.seek(0) # 如果是空的，可以考慮讓記得讓游標移到最開始
    content_list = f.read()

# *將文章分割成單字，刪除stopwords，並查詢詞性
# mytext = "Hello Adam, how are you doing? I hoped everything would be going well. Today is a good day, saw you dude."
# ! 不對，大小寫應該要分開，但句首跟專有名詞分不清楚
tokens = [x for x in word_tokenize(content_list)]  # 將文章轉成單字列表
stop_words = set(stopwords.words('english')) # 設定stopwords語系
tagged_sent = pos_tag(tokens)  # nltk pos_tag抓取詞性功能 (有點可惜沒有根據上下文，還是或許其實有) #! 不確定刪除stopword前執行，會好一點?
tokens_free1 = [x for x in tagged_sent if not x in list(stop_words)] # 刪除stopwords (會刪除this不會刪除This)
tokens_free2 = [x for x in tokens_free1 if not x in [x.capitalize() for x in list(stop_words)]] # 刪除stopwords的Capital版 # 所以雙重生成式可以的耶!
# print(tokens_free2)

# print(get_wordnet_pos(tagged_sent[0][1]))

# *詞性篩選: 將詞性抓取n,v,a,r，並轉成pos=的關鍵字，最後用lem還原成原型詞
# @link [NLP入门（三）词形还原（Lemmatization） - 山阴少年 - 博客园](https://www.cnblogs.com/jclian91/p/9898511.html) at 2021/8/15
wnl = WordNetLemmatizer()
words_lem = []
words_NNP = []  # 專有名詞列表，但其實算是Capitalize列表，因目前無法分辨非專有名詞
for tag in tagged_sent:
    wordnet_pos = get_wordnet_pos(tag[1])
    if wordnet_pos == None:  # 不過這樣就直接省略掉所有n,v,a,r,以外的詞類了
        continue
    if wordnet_pos == 'NNP':
        words_NNP.append(wordnet_pos)
        continue
    words_lem.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # wordnet_pos=None會出問題

# *將列表轉成小寫，去除list重複資料，產生無重複list
words_lem_low = [x.lower() for x in words_lem]
words_lem_cate = list(set(words_lem_low))
# *刪除我還認為的贅字
trash_words = ["'ve","n't","'m","'s"]
words_lem_cate = [x for x in words_lem_cate if not x in list(trash_words)]
print(words_lem_cate)

# *計算字詞出現次數 - 擇一使用 (使用FreqDist會自動刪除重複資料)
""" 
lem_words_count = {i: lem_words.count(i) for i in lem_words_cate}
lem_words_count = sorted(lem_words_count.items(), key=lambda x: x[1], reverse=True)
print(lem_words_count) 
"""
""" 
fdist = FreqDist(lem_words)
freqWords = fdist.most_common()
print(freqWords) 
"""

# *刪除10000常見的文字
filename2 = "google-10000-english-usa.txt"
with open(filename2, mode="r", encoding="utf-8") as f:
    # f.seek(0) # 如果是空的，可以考慮讓記得讓游標移到最開始
    content_list2 = f.read()
tokens_ck = [x for x in word_tokenize(content_list2)]

list_fl = [x for x in words_lem_cate if not x in tokens_ck]
print(list_fl)

# @link [Python深度學習筆記(五)：使用NLTK進行自然語言處理. 安裝NLTK | by Yanwei Liu | Medium](https://yanwei-liu.medium.com/python%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%BA%94-%E4%BD%BF%E7%94%A8nltk%E9%80%B2%E8%A1%8C%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86-24fba36f3896) at 2021/8/15

