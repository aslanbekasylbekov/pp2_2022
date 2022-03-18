s = input()
upper = 0
lower = 0
for i in s:
    if i.isupper(): 
        upper += 1
    if i.islower(): 
        lower += 1
eval("print(upper,lower)")
