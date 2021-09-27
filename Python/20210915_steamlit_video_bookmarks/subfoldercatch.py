# %%
import pathlib
from pathlib import Path
import os

# path = Path()
# for p in path.glob("*"):
#     print(p.name)

# for p in path.rglob("*"):
#     print(p.name)

inFolder = "scan/"
outFolder = "res/"
inFolderPath = pathlib.Path(__file__).parents[0].joinpath(inFolder)
outFolderPath = pathlib.Path(__file__).parents[0].joinpath(outFolder)
subfolders = os.listdir("./scan")

for i in range(len(subfolders)):
    subfoldersPath = "./scan/" + subfolders[i]
    folderIter = inFolderPath.joinpath(subfolders[i]).iterdir()
    folerIterlist = list(enumerate(folderIter))
    print(folerIterlist)

# %%
import os

subfolders = os.listdir("./scan")
for i in range(len(subfolders)):
    subfoldersPath = "./scan/" + subfolders[i]
    subfolder = subfolders[i]
    print(subfolder)
    subfolderimgs = os.listdir(subfoldersPath)
    print(subfolderimgs)
# %%
