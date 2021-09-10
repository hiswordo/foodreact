# %%
import pyttsx3

# 初始化
engine = pyttsx3.init()
voices = engine.getProperty("voices")  # [<pyttsx3.voice.Voice at 0x4a5b760>]
# engine.setProperty('voice', voice.id) # 未測:更換人聲
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# %%
# 設定
# 語速控制
rate = engine.getProperty("rate")  # 預設:200/min
# engine.setProperty('rate', rate-20) # rate被減少20
# engine.setProperty('rate', 30) # 直接設定成30語速

# 音量控制
volume = engine.getProperty('volume') # 預設:0.2
# engine.setProperty('volume', volume+0.25) # 增加0.25，範圍0~1

# %%
# 預設要念的詞
engine.setProperty('voice', voices[4].id) 
engine.say("hello world")
# engine.say("你好，世界")

# 朗讀一次
engine.runAndWait()

# %%
engine.say("語音合成開始")
engine.say("我會說中文了，開森，開森")
engine.say('我会说中文了，开森，开森')
engine.runAndWait()

engine.say("The quick brown fox jumped over the lazy dog.")
engine.runAndWait()

# %%
# Saving Voice to a file
# // engine.save_to_file('Hello World', './test.mp3')

# @link [[Python]如何Text to Speech: pyttsx3, gTTS - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10251544) at 2021/9/10
# @link [Speech Synthesis and Voice Recognition with PyTTSX3 and PocketSphinx - YouTube](https://www.youtube.com/watch?v=iUfxHJ072qI&loop=0) at 2021/9/10

# %%
