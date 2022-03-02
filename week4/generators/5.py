def generates(n):
    while n>=0:
        yield n
        n-=1
n = int(input())
for x in generates(n):
    print(x)
