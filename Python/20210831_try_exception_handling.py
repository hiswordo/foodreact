
# @link [Python exception handling ⚠️ - YouTube](https://www.youtube.com/watch?v=j_q6NGOwDJo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=30) at 2021/8/31


try:
    numerator = int(input("up number:"))
    denumerator = int(input("down number:"))
    result = numerator/denumerator
except ZeroDivisionError as e:
    print(e)
    print("denumrator can't be 0")
except ValueError as e:
    print(e)
    print("gotta to be a number, idiot!")
except Exception as e:
    print(e)
    print("sth went wrong?")
else:
    print(f"{result=}")