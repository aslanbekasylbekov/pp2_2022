def generates(n):
    i = 0
    while i <= n:
        yield i
        i+=2
n = int(input())
a = []
for x in generates(n):
    a.append(str(x))
print (','.join(a))