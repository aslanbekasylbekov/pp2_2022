n = int(input())
a = []
ans = ""
for i in range(0,n):
    s = input()
    if "@gmail.com" in s:
        b = s.strip("@gmail.com")
        a.append(b)
print(*a,sep='\n')