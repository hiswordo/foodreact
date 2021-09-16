
# @link [Using Pathlib in Python - YouTube](https://www.youtube.com/watch?v=DOgjN7RmHds&loop=0) at 2021/9/12
# %%
import pathlib
pathlib.Path(__file__) # 這次是 WindowsPath('g:/my_coding/Python/20210912_modules_pathlib.py')

windows_path = pathlib.WindowsPath(__file__) # WindowsPath('g:/my_coding/Python/20210912_modules_pathlib.py')
windows_pure_path = pathlib.PureWindowsPath(__file__) # PureWindowsPath('g:/my_coding/Python/20210912_modules_pathlib.py')

# %%
# grab part of path
windows_path.parts # tuple ('g:\\', 'my_coding', 'Python', '20210912_modules_pathlib.py')

windows_path.parent.parent # WindowsPath('g:/my_coding')
windows_path.parents[1] # WindowsPath('g:/my_coding')

# %%
# 創建資料夾路徑pathlib
data_folder = pathlib.Path(__file__).parents[0].joinpath('data_video')
print(data_folder) # g:\my_coding\Python\data_video

# 如果沒有路徑沒有資料夾則創建
if not data_folder.exists():
    data_folder.mkdir()

# touch創建檔案，exist_ok表示"若存在，覆蓋過去也沒關係"
# mkdir創建資料夾，也可以這樣用
data_folder.joinpath('this_file.txt').touch(exist_ok=True) 
data_folder.joinpath('this_file').mkdir(exist_ok=True) 

# %%
# From here lets iterate through the folder.
for file_obj in data_folder.iterdir():

    # Let's ask some questions about each object.
    print("+"*80)
    print(file_obj)
    print("Are you a directory? " + str(file_obj.is_dir()))
    print("Are you a file? " + str(file_obj.is_file()))
    print("Are you a symbolic link? " + str(file_obj.is_symlink()))
    print("File Drive is: " + str(file_obj.drive))
    print("File Anchor is: " + str(file_obj.anchor))
    print("File Stem is: " + str(file_obj.stem))
    print("File Suffix is: " + str(file_obj.suffix))
    print("File Name is: " + str(file_obj.name))

# %%
# Here are some useful methods.

# Grab the Current Working Directory.
str(pathlib.Path.cwd()) # 'g:\\my_coding\\Python'
print(str(pathlib.Path.cwd())) # g:\my_coding\Python
# Grab the File Path of THIS script.
str(pathlib.Path(__file__)) # 'g:\\my_coding\\Python\\20210912_modules_pathlib.py'
# Grab the System home path.
print("Home Path is: " + str(pathlib.Path.home()))

# %%
# `absolute` takes a partial path and makes it a full path.
print("My Partial Path looks like this before `absolute`: " + str(pathlib.Path("data")))
print("My Partial Path looks like this after `absolute`: " + str(pathlib.Path("data").absolute()))

# %%
# resolve() 抓取完整路徑，幫你把剩下的填完整，整理斜線
# `resolve` will do things like remove `..` or 
# change windows path to unix paths and vice versa.
print(pathlib.Path('my_coding/../20210912_modules_pathlib.py').resolve())
print(pathlib.Path('my_coding/20210912_modules_pathlib.py').resolve())
print(pathlib.Path("G:/my_coding/Python/20210912_modules_pathlib.py").resolve())

# %%
# ---[ 檔案路徑: 列出當下所有資料夾 Listing subdirectories ]---
p = pathlib.Path('.')
[x for x in p.iterdir() if x.is_dir()]

# %%
# ---[ 檔案列表: 列出 data_folder 底下的所有檔案 ]---
# 純檔名，不包含路徑
folderIter = pathlib.Path(__file__).parents[0].joinpath("res/").iterdir()
for ingName in folderIter:
    print(str(ingName.parts[-1]))

# 特定檔案txt，並包含路徑
data_folder = pathlib.Path(__file__).parents[0].joinpath('data_video')
list(data_folder.glob('**/*.txt'))


# %%
# q = pathlib.Path('/data_video') / 'second' / 'third'
# print(q.resolve())
# with q.open() as f: f.readline()


# %%
