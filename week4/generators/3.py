def generates(n):
    for i in range(0,n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        else:
            continue
n = int(input())
for x in generates(n):
    print(x)