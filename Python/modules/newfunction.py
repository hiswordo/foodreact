
# 尚在測試的模組

def dir_remodule(listin):
    removelist = ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
    for i in removelist:
        listin.remove(i)
    return listin

# for testing
def sayhello(qoute1):
    print(f'Hello World! {qoute1}')
    
rock1 = 30

# if __name__ == '__main__':
#     print("測試程式碼")
# print("about module name: ", __name__) 