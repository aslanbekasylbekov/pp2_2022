def func(s):
    a = []
    for i in s:
        if i not in a:
            a.append(i)
    return a
s = list(input().split())
print(*func(s))