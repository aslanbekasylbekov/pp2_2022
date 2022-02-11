import math
n = list(map(int, input().split()))
a = []
def fun(a):
    return math.sqrt(((a[0] - n[0])**2) + ((a[1] - n[1])**2))
m = int(input())
for i in range(m):
    s = list(map(int, input().split()))
    a.append(s)
a.sort(key=fun)
for i in range(m):
    for j in range(2):
        print(a[i][j], end=" ")
    print()