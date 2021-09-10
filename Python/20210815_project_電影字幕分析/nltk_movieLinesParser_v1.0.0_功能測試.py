# ne_chunk 命名实体识别 測試:未完成

from nltk import ne_chunk
from nltk import pos_tag
from nltk import word_tokenize
input = "Edison went to Tsinghua University today."

print(ne_chunk(pos_tag(word_tokenize(input))))

# FreqDist 功能測試
# @link [FreqDist - nltk - Python documentation - Kite](https://www.kite.com/python/docs/nltk.FreqDist) at 2021/8/15
""" fdist = FreqDist(lem_words)
# print(FreqDist(lem_words)) # <FreqDist with 41 samples and 60 outcomes>
fdist1 = fdist.most_common(10) #出現頻率最高的10個單字
# print(fdist1)
fdist2 = fdist.most_common() #! 不填數字就全部出現了..
print(fdist2)
# fdist2 = fdist.hapaxes() # Return a list of all samples that occur once (只出現一次的)
 """

# stem 與 lem 功能測試
"""
# stem還原超小耶...才ing而已
ps = PorterStemmer()
stemmer_words = []
for x in mytext_words:
    stemmer_words.append(ps.stem(x))
# print(stemmer_words)

# lem (stem升級版)
lem = WordNetLemmatizer()
print(lem.lemmatize("gone", pos="v"))
print(lem.lemmatize("leaves", pos="n"))
print(lem.lemmatize("better", pos="a"))
print(lem.lemmatize("playing", pos="r"))
 """
 
# stop_words 列表
'''
{ "off", "weren", "yours", "had", "more", "did", "here", "this", "hadn't", "our", "in",
    "are", "who", "both", "that'll", "under", "an", "will", "d", "m", "having", "but",
    "ve", "if", "on", "hasn", "it", "being", "only", "doing", "between", "hasn't",
    "where", "all", "those", "o", "mightn't", "or", "because", "their", "its", "such", "and",
    "when", "ours", "now", "couldn", "ll", "as", "during", "after", "again", "of", "mustn",
    "against", "haven", "shouldn", "doesn't", "shan't", "he", "wouldn", "you've", "mustn't",
    "can", "shan", "once", "needn't", "some", "be", "weren't", "about", "too", "won't", "just",
    "until", "s", "t", "won", "wasn", "my", "why", "your", "nor", "these", "further", "which",
    "ain", "you'd", "didn", "should", "down", "isn't", "haven't", "at", "into", "not", "there",
    "few", "it's", "itself", "needn", "wasn't", "wouldn't", "his", "were", "do", "theirs",
    "while", "was", "ma", "ourselves", "she's", "then", "over", "same", "they", "above",
    "most", "to", "shouldn't", "for", "she", "you'll", "how", "with", "mightn", "me",
    "from", "a", "by", "whom", "have", "any", "very", "up", "aren", "has", "should've",
    "aren't", "no", "doesn", "herself", "yourselves", "them", "before", "does", "don",
    "you", "below", "you're", "is", "that", "re", "am", "i", "each", "through", "her",
    "been", "out", "don't", "myself", "the", "didn't", "isn", "himself", "than",
    "yourself", "hers", "own", "other", "we", "hadn", "themselves", "y", "so",
    "him", "what", "couldn't", }'''

""" 舊版get_wordnet_pos def多此一舉
def get_wordnet_pos(tag):
    def startswith(fstletter):
        return fstletter == self[0]
    if tag.startswith("A"):
        return "a"  #! pos=小寫英文
    elif tag.startswith("V"):
        return "v"
    elif tag.startswith("N"):
        return "n"
    elif tag.startswith("R"):  # 應該是副詞
        return "r"
    else:
        return None
"""

# 通篇文章
""" This will be the final boarding call for flight to London, Heathrow.
I'm not even gonna say it, Kate.
Then it'll be like I never left.
Wait.
I have a really bad feeling about this.
About the plane? You think it's gonna crash? Don't say that.
No. Look, I know that we've talked about this a thousand times
and we agreed that going to London was the right thing to do.
But in my heart...this feels wrong.
Don't go, Jack.
You mean don't go at all?
Well, what...what about my internship?
Believe me, I know...I know what an incredible opportunity this is for you. """

# 拆成單字列表後，刪除stop word再判斷詞性
list01 = [
    ("final", "JJ"),
    ("boarding", "NN"),
    ("call", "NN"),
    ("flight", "NN"),
    ("London", "NNP"),
    (",", ","),
    ("Heathrow", "NNP"),
    (".", "."),
    ("'m", "VBP"),
    ("even", "RB"),
    ("gon", "VBG"),
    ("na", "TO"),
    ("say", "VB"),
    (",", ","),
    ("Kate", "NNP"),
    (".", "."),
    ("'ll", "MD"),
    ("like", "VB"),
    ("never", "RB"),
    ("left", "VBN"),
    (".", "."),
    ("Wait", "NNP"),
    (".", "."),
    ("really", "RB"),
    ("bad", "JJ"),
    ("feeling", "NN"),
    (".", "."),
    ("plane", "NN"),
    ("?", "."),
    ("think", "VBP"),
    ("'s", "POS"),
    ("gon", "NN"),
    ("na", "TO"),
    ("crash", "NN"),
    ("?", "."),
    ("n't", "RB"),
    ("say", "VB"),
    (".", "."),
    (".", "."),
    ("Look", "VB"),
    (",", ","),
    ("know", "VB"),
    ("'ve", "VBP"),
    ("talked", "VBN"),
    ("thousand", "JJ"),
    ("times", "NNS"),
    ("agreed", "VBD"),
    ("going", "VBG"),
    ("London", "NNP"),
    ("right", "JJ"),
    ("thing", "NN"),
    (".", "."),
    ("heart", "NN"),
    ("...", ":"),
    ("feels", "NNS"),
    ("wrong", "RB"),
    (".", "."),
    ("n't", "RB"),
    ("go", "VB"),
    (",", ","),
    ("Jack", "NNP"),
    (".", "."),
    ("mean", "VBP"),
    ("n't", "RB"),
    ("go", "VB"),
    ("?", "."),
    ("Well", "RB"),
    (",", ","),
    ("...", ":"),
    ("internship", "NN"),
    ("?", "."),
    ("Believe", "NNP"),
    (",", ","),
    ("know", "VBP"),
    ("...", ":"),
    ("know", "VBP"),
    ("incredible", "JJ"),
    ("opportunity", "NN"),
    (".", "."),
]
# 拆成單字列表後，直接判斷詞性
list_ck = [
    ("This", "DT"),
    ("will", "MD"),
    ("be", "VB"),
    ("the", "DT"),
    ("final", "JJ"),
    ("boarding", "NN"),
    ("call", "NN"),
    ("for", "IN"),
    ("flight", "NN"),
    ("to", "TO"),
    ("London", "NNP"),
    (",", ","),
    ("Heathrow", "NNP"),
    (".", "."),
    ("I", "PRP"),
    ("'m", "VBP"),
    ("not", "RB"),
    ("even", "RB"),
    ("gon", "VB"),
    ("na", "TO"),
    ("say", "VB"),
    ("it", "PRP"),
    (",", ","),
    ("Kate", "NNP"),
    (".", "."),
    ("Then", "RB"),
    ("it", "PRP"),
    ("'ll", "MD"),
    ("be", "VB"),
    ("like", "IN"),
    ("I", "PRP"),
    ("never", "RB"),
    ("left", "VBD"),
    (".", "."),
    ("Wait", "NNP"),
    (".", "."),
    ("I", "PRP"),
    ("have", "VBP"),
    ("a", "DT"),
    ("really", "RB"),
    ("bad", "JJ"),
    ("feeling", "VBG"),
    ("about", "IN"),
    ("this", "DT"),
    (".", "."),
    ("About", "IN"),
    ("the", "DT"),
    ("plane", "NN"),
    ("?", "."),
    ("You", "PRP"),
    ("think", "VBP"),
    ("it", "PRP"),
    ("'s", "VBZ"),
    ("gon", "JJ"),
    ("na", "TO"),
    ("crash", "VB"),
    ("?", "."),
    ("Do", "VBP"),
    ("n't", "RB"),
    ("say", "VB"),
    ("that", "IN"),
    (".", "."),
    ("No", "DT"),
    (".", "."),
    ("Look", "VB"),
    (",", ","),
    ("I", "PRP"),
    ("know", "VBP"),
    ("that", "IN"),
    ("we", "PRP"),
    ("'ve", "VBP"),
    ("talked", "VBN"),
    ("about", "IN"),
    ("this", "DT"),
    ("a", "DT"),
    ("thousand", "JJ"),
    ("times", "NNS"),
    ("and", "CC"),
    ("we", "PRP"),
    ("agreed", "VBD"),
    ("that", "IN"),
    ("going", "VBG"),
    ("to", "TO"),
    ("London", "NNP"),
    ("was", "VBD"),
    ("the", "DT"),
    ("right", "JJ"),
    ("thing", "NN"),
    ("to", "TO"),
    ("do", "VB"),
    (".", "."),
    ("But", "CC"),
    ("in", "IN"),
    ("my", "PRP$"),
    ("heart", "NN"),
    ("...", ":"),
    ("this", "DT"),
    ("feels", "VBZ"),
    ("wrong", "JJ"),
    (".", "."),
    ("Do", "VBP"),
    ("n't", "RB"),
    ("go", "VB"),
    (",", ","),
    ("Jack", "NNP"),
    (".", "."),
    ("You", "PRP"),
    ("mean", "VBP"),
    ("do", "VBP"),
    ("n't", "RB"),
    ("go", "VB"),
    ("at", "IN"),
    ("all", "DT"),
    ("?", "."),
    ("Well", "NNP"),
    (",", ","),
    ("what", "WP"),
    ("...", ":"),
    ("what", "WP"),
    ("about", "IN"),
    ("my", "PRP$"),
    ("internship", "NN"),
    ("?", "."),
    ("Believe", "NNP"),
    ("me", "PRP"),
    (",", ","),
    ("I", "PRP"),
    ("know", "VBP"),
    ("...", ":"),
    ("I", "PRP"),
    ("know", "VBP"),
    ("what", "WP"),
    ("an", "DT"),
    ("incredible", "JJ"),
    ("opportunity", "NN"),
    ("this", "DT"),
    ("is", "VBZ"),
    ("for", "IN"),
    ("you", "PRP"),
    (".", "."),
]
""" list_fl = []
for x in list01:
    for y in list_ck:
        if x[0] == y[0] and x[1] != y[1]:
            list_fl.append(x)

print(list_fl) """
# 差異:list_fl
""" [('gon', 'VBG'), ('gon', 'VBG'), ('like', 'VB'), ('left', 'VBN'), ('feeling', 'NN'), ("'s", 'POS'), ('gon', 'NN'), ('gon', 'NN'), ('crash', 'NN'),
('know', 'VB'), ('know', 'VB'), ('know', 'VB'), ('feels', 'NNS'), ('wrong', 'RB'), ('Well', 'RB')] """