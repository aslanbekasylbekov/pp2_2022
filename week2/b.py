num = int(input())
a = []
for i in input().split():
    a.append(int(i))
    a.sort()
print(a[-1]*a[-2])
