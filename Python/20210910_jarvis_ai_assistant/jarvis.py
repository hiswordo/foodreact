# %%
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# import wikipedia
# import pyjokes
import pyautogui

from plyer import notification
from bs4 import BeautifulSoup
import requests

from pathlib import Path

path = Path(
    __file__
)  # WindowsPath('g:/my_coding/Python/20210910_jarvis_ai_assistant/jarvis.py')
folderpath = (
    Path.cwd()
)  # WindowsPath('g:/my_coding/Python/20210910_jarvis_ai_assistant')


def rAinB_lower(a, b):
    return a.lower() in b.lower()


# @link [Build your own J.A.R.V.I.S in Python [Full Code + Video] - DEV Community](https://dev.to/thenerdydev/build-your-own-j-a-r-v-i-s-in-pyhon-full-code-video-4o1b) at 2021/9/11

# @link [Voice Assistant in Python | How To Build Desktop Voice Assistant in Python](https://www.analyticsvidhya.com/blog/2020/11/build-your-own-desktop-voice-assistant-in-python/) at 2021/9/11

engine = pyttsx3.init()
voices = engine.getProperty("voices")
# engine.setProperty('voice', voices[1].id)


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("recognition is on....")
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(voice).lower()
            print("this is the query that was made....", query)
            return query
        except Exception as ex:
            print("An exception occurred", ex)


def report_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return current_time


def make_request(url):
    response = requests.get(url)
    return response.text


def voice_check(msg):
    ask = 1
    while ask == 1:
        speak_va("Do you mean" + msg)
        answer = input_query()
        if "no" in answer:
            speak_va("Tell me the correct one")
            msg = input_query()
        elif "yes" in answer:
            ask = 0
        else:
            speak_va("sorry, not clear")
            ask = 1
    return msg


asktime = 1

# %%
def activate_va():
    if asktime == 1:
        speak_va("Hi there, anything help?")
    else:
        speak_va("anything help?")
    user_query = input_query()
    if user_query == None:
        user_query = "Saying Nothing"
    print("user query ....", user_query)
    if "time" in user_query:  # "tell me what time it is" 就也可以
        current_time = report_time()
        print(f"the current time is {current_time}")
        speak_va(f"the current time is {current_time}")
    elif "open website" in user_query:
        # speak_va(
        #     "Please type the name of the website that you want to open (specify the full url) \n"
        # )
        speak_va("name of website? \n")
        # website_name = input() + ".com"
        website_name = input_query()
        website_name_checked = voice_check(website_name) + ".com"
        print(website_name_checked)
        webbrowser.get(
            "C:/Program Files (x86)/Microsoft/Edge/Application/92.0.902.84/msedge.exe %s"
        ).open(website_name_checked)
        # 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(website_name)
        # 沒有加%s: webbrowser.Error: could not locate runnable browser
        speak_va(f"{website_name_checked} opened.")
        """ elif 'wikipedia' in user_query:
            speak_va("Searching on Wikipedia")
            user_query = user_query.replace('wikipedia', ' ')
            result = wikipedia.summary(user_query, sentences=4)
            print(result)
            speak_va(result)
        elif 'joke' in user_query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak_va(random_joke) """
    elif "screenshot" in user_query:
        image = pyautogui.screenshot()
        imgpath = folderpath / "screenshot.png"
        image.save(imgpath)
        speak_va("Screenshot has been taken.")
    elif "search" in user_query:
        speak_va("Search for?")
        search_term = input_query()
        search_url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get(
            "C:/Program Files (x86)/Microsoft/Edge/Application/92.0.902.84/msedge.exe %s"
        ).open(search_url)
        speak_va(f"here are the results for: {search_term}")
    elif 'covid status' in user_query:
        # %%
        html_data = make_request('https://www.worldometers.info/coronavirus/')
        # print(html_data)
        soup = BeautifulSoup(html_data, 'html.parser')
        total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
        total_cases = total_global_row.find_all('td')[2].get_text()
        new_cases = total_global_row.find_all('td')[3].get_text()
        total_recovered = total_global_row.find_all('td')[6].get_text()
        print('total cases : ', total_cases)
        print('new cases', new_cases[1:]) # 去掉+號[1:]
        print('total recovered', total_recovered)
        
        notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
        notification.notify(
        title="COVID-19 Statistics",
        message=notification_message,
        timeout=5
        )
        speak_va("here are the stats for COVID-19")
        # %%
    elif rAinB_lower("no", user_query):  # 這樣就會有缺點，因為稍微提到像是not就會觸發了
        speak_va("See you next time!")
        return False
    else:
        speak_va("Say again?")
        pass
    return True


running = True
# *如果function()沒有回傳的話，會自動回傳None
while running:
    running = activate_va()
    asktime = 2


# @link [Learn To Create AI Assistant (JARVIS) With Python | Udemy](https://www.udemy.com/course/learn-to-create-ai-assistant-jarvis-with-python/) at 2021/9/11


# 尚未研究
# @link [詳解Python中pyautogui庫的最全使用方法_程式設計_程式人生](https://www.796t.com/article.php?id=17523) at 2021/9/13
