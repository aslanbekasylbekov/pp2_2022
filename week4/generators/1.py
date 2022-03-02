def generates(N):
    for i in range(N+1):
        yield i**2
N = int(input())
print()
for x in generates(N):
    print(x)