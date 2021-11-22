# %%
from mymodules.newfunction import *

rAinB_lower("a", "abc")

# %%
import string

unmap = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newSentence = ""
for x in unmap:
    # if x == (" " or "." or "," or "'" or"(" or ")"):
    if x == " " or x in string.punctuation:
        newSentence += x
    else:
        # if ord(x)+2 > 122:
        #     newOrd = 96 + (ord(x)+2) % 122
        # else: newOrd = ord(x) + 2
        newOrd = ord(x) + 2
        newlett = chr(newOrd)
        newSentence += newlett
newSentence.replace("{", "a").replace("|", "b")

# %%
unmap = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newSentence = ""
for x in unmap:
    trantab = str.maketrans(x, chr(ord(x) + 2))
    if x.isalpha():
        newSentence += x.translate(trantab).replace("{", "a").replace("|", "b")
    else:
        newSentence += x
newSentence

# %%
def combinations(*items):
    newlist = [x for x in items if x != 0]
    if len(items) == 1:
        return items[0]
    y = 1
    for x in newlist:
        y = y * x
    return y


combinations(8)
# %%
list = []
for x in range(97, 123):
    list.append(chr(x))
list
print(96 + 123 % 122)
# ord('z')
# print(122-97)

# %%
str_1 = ","
import string

punc = string.punctuation  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
if str_1 in punc:
    print("is punctuation")

# %%
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

strr = "this is string example....wow!!!"
print(strr.translate(trantab))

# %%
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b
# 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b
# 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b
# 49 = 0011 0001
print("3 - c 的值为：", bin(c))

c = ~a
# -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2
# 240 = 1111 0000
print("5 - c 的值为：", c)

c = a >> 2
# 15 = 0000 1111
print("6 - c 的值为：", c)

# %%
