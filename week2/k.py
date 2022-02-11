s = input()
a = []
b = set(s.split())
a.extend(b)
a.sort()
print(len(a))
for i in a:
    if i.isalpha():
        print(i)
    else:
        print(i[:-1])
