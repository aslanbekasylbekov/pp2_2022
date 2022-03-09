import re
txt = input()
x=re.findall('[A-Z][^A-Z]*',txt)
ans = ""
for i in x:
    ans += i +" "
print(ans)