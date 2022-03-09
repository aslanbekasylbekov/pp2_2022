import re
def func(txt):
    x = r'[A-Z]+[a-z]*'
    arr = re.findall(x, txt)
    arr = [i.lower() for i in arr]
    txt = '_'.join(arr)
    return txt
txt = input()
print(func(txt))