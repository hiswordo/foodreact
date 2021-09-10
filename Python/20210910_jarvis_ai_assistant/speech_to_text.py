import speech_recognition as sr

# SpeechRecognition系統自身並沒有語音識別功能，因此我們需要為SpeechRecognition安裝一款語音識別引擎
# pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl
# 很爛款? pip install pocketsphinx-0.1.15-cp38-cp38-win_amd64.whl

# ---< 麥克風輸入 >---
# 英文、中文語音測試，順利
# **google語音庫**
def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('recognition is on....')
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(voice).lower()
            # query = recognizer.recognize_google(voice,language="zh-CN")
            print('this is the query that was made....', query)
            # return query
        except Exception as ex:
            print('An exception occurred', ex)

# recognize_sphinx(voice)
# An exception occurred missing PocketSphinx module: ensure that PocketSphinx is set up correctly.

# ---< wav檔案輸入 >---
# 英文、中文語音測試，順利
""" import speech_recognition as sr
r = sr.Recognizer()
# WAV = sr.AudioFile('./20210910_jarvis_ai_assistant/res/speech_english.wav')
WAV = sr.AudioFile('./20210910_jarvis_ai_assistant/res/speech_chinese.wav')
with WAV as source:
    audio = r.record(source)
# print(r.recognize_google(audio))
# everyone this is speech recognition task welcome to the new world
print(r.recognize_google(audio, language="zh-TW"))
# 你好這裡是中文測試音天的天氣真好
# print(r.recognize_google(audio, show_all=True)) # show列出一堆回傳資料 """

# recognize_sphinx測試結果...如傳聞，真的差...別用
# print(r.recognize_sphinx(audio,language="en-US"))
# both of you on this is bitch their car condition that's welcome to the new war
# print(r.recognize_sphinx(audio,language="zh-CN"))
# 然而 这是 中 应 正视 并 将 这 显示 正常



# ------以下尚未測試------
# 指定要轉換的音頻源文件（english.wav）
""" from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
 """
# 定義SpeechRecognition對象並獲取音頻源文件（english.wav）中的數據
""" r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file """

# 使用CMU Sphinx引擎去識別音頻
""" try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e)) """

# 使用Microsoft Bing Voice Recognition引擎去識別音頻
""" BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
 """


# -*- coding: utf-8 -*-
# import speech_recognition as sr
# AUDIO_FILE = "11.wav"
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file

# res = r.recognize_sphinx(audio)
# res1 = res.split(" ")
# # for each in res1:
# print(" ".join(res1))

# 補充:
# @link [PocketSpinx添加中文语音识别包_朽be-CSDN博客](https://blog.csdn.net/yuxuwen1234/article/details/104529675) at 2021/9/11
# @link [痞子衡嵌入式：語音處理工具pzh-speech誕生記（5）- 語音識別實現(SpeechRecognition, PocketSphinx0.1.15) - 碼上快樂](https://zh.codeprj.com/blog/9220de1.html) at 2021/9/11