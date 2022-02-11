a = []
res = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        a.append(n)
for i in range(int(len(a)/2)):
    res.append(a[i]+a[len(a)-i-1])
if len(a)%2 != 0:
    res.append(a[int(len(a)/2)])
print(*res)