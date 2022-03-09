import re
txt = input()
x = re.findall('[a-z][^_]*',txt)
ans = ""
for i in x:
    ans += i.capitalize()
print(ans)