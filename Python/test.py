""" from functools import reduce
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5]) 
print(sum2) """

""" for x in range(1,4):
    print(x)

lislist = [7,3,5,9]
print(list(enumerate(lislist))[0][0]) """

# [[[1, 2], [1, 3], [1, 5]], [[1, 2, 4, 8], [1, 5]]]
# [[1, 2, 3, 5, 6, 10, 15, 30], [1, 2, 4, 5, 8, 10, 20, 40]]
""" def __findFactors(self):
    ultiResult = []
    outresult = []
    for j in range(len(self.mylist)):
        if len(self.mylist[j]) == 1:
            outresult.append(self.mylist[j])
        else:
            result = self.mylist[j][0]
            for i in range(1,len(self.mylist[j])):
                result = self.multiplylist(result, self.mylist[j][i])
            outresult = result
        ultiResult.append(sorted(outresult))
    return ultiResult """

# [{2: 1, 3: 1, 5: 1}, {2: 3, 5: 1}]
# [[[1, 2], [1, 3], [1, 5]], [[1, 2, 4, 8], [1, 5]]]
# 建立num的質因數所有次方的清單

""" original = [{2: 1, 3: 1, 5: 1}, {2: 3, 5: 1}]

def prlist():
    
    mylist = []
    for i in range(len(original)):
        a = list(original[i].keys())
        b = original[i]
        outterlist = []
        for x in a:
            pow = 0 
            innerlist = []
            for pow in range(b[x]+1):
                innerlist.append(x**pow)
                # print(f"{innerlist=}")
            outterlist.append(innerlist)
            # print(f"{outterlist=}")
        mylist.append(outterlist)
    return mylist """

# %%
import pandas as pd

selected_year = 2001
# def load_data(year):
url = (
    "https://www.basketball-reference.com/leagues/NBA_"
    + str(selected_year)
    + "_per_game.html"
)
html = pd.read_html(url, header=0)  # <class 'list'>
df = html[0]  # <class 'pandas.core.frame.DataFrame'>
# df.Tm.unique()
df.corr()
# raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
# raw = raw.fillna(0)
# playerstats = raw.drop(['Rk'], axis=1)
# df.iloc[21:27]
# return playerstats
# playerstats = load_data(selected_year)
# playerstats

# %%
# 函數中的函數
def callother(func):
    return func()


def add():
    print("add")


callother(add)
# %%
def run_op(func, *args):
    func(*args)


def add(*args):
    result = 0
    for arg in args:
        result += arg
    print(result)


def multi(*args):
    result = 1
    for arg in args:
        result *= arg
    print(result)


# 利用內建函數，sun原來可以傳入
def sum_args(*args):  # 定義函式 → 函式取用任意數量的位置引數 → 使用 sum() 函式來計算「引數總和」
    print(args)  # (3, 4, 2) tuple耶
    print(sum(args))


run_op(add, 3, 4, 7, 8)  # 22
run_op(multi, 3, 4, 2)  # 24
run_op(sum_args, 3, 4, 2)  # 24

# %%

# Case A in B without Case Sensitive
def rAinB(a, b):
    return a.lower() in b.lower()

print(rAinB("no","Saying Nothing"))


# %%
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('Using Pathlib in Python', limit = 1)
urlink = dict(videosSearch.result()['result'][0])['link']
print(urlink)

# %%
import pandas as pd
df = pd.read_xml(("./res/[MISM-082].nfo"))
df
# %%
from youtubesearchpython import VideosSearch
def searchYT(videoName):
    # 上網並搜索 影片名稱網址、影片頻道名稱、合併 網址與標記時間
    videosSearch = VideosSearch(videoName, limit=1)
    urlili = dict(videosSearch.result()["result"][0])
    print(f'{urlili["link"]}')
    print(f'{urlili["id"]}')
    print(f'{urlili["title"]}')
    print(f'{urlili["publishedTime"]}')
    print(f'{urlili["duration"]}')
    print(f'{urlili["viewCount"]["text"]}')
    print(f'{urlili["thumbnails"][0]["url"]}')
    print(f'{urlili["descriptionSnippet"][0]["text"]}')
    print(f'{urlili["channel"]["name"]}')
    print(f'{urlili["channel"]["id"]}')
    print(f'{urlili["channel"]["thumbnails"][0]["url"]}')
    print(f'{urlili["channel"]["link"]}')


searchYT("Intermediate Python Programming Course")
# %%
{
    "result": [
        {
            "type": "video",
            "id": "K4DyBUG242c",
            "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release]",
            "publishedTime": "5 years ago",
            "duration": "3:28",
            "viewCount": {
                "text": "389,673,774 views",
                "short": "389M views"
            },
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/K4DyBUG242c/hqdefault.jpg?sqp=-oaymwEjCOADEI4CSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBkTusCwcZQlmVAaRQ5rH-mvBuA1g",
                    "width": 480,
                    "height": 270
                }
            ],
            "descriptionSnippet": [
                {
                    "text": "NCS: Music Without Limitations NCS Spotify: http://spoti.fi/NCS Free Download / Stream: http://ncs.io/onandon \u25bd Connect with\u00a0..."
                }
            ],
            "channel": {
                "name": "NoCopyrightSounds",
                "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                "thumbnails": [
                    {
                        "url": "https://yt3.ggpht.com/a-/AOh14GhS0G5FwV8rMhVCUWSDp36vWEvnNs5Vl97Zww=s68-c-k-c0x00ffffff-no-rj-mo",
                        "width": 68,
                        "height": 68
                    }
                ],
                "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
            },
            "accessibility": {
                "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release] by NoCopyrightSounds 5 years ago 3 minutes, 28 seconds 389,673,774 views",
                "duration": "3 minutes, 28 seconds"
            },
            "link": "https://www.youtube.com/watch?v=K4DyBUG242c",
            "shelfTitle": null
        },
    ]
}