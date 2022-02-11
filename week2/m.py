a = []
while True:
    s = input()
    if s == '0':
        break
    else:
        a.append(s.split()[2]+' '+s.split()[1]+' '+s.split()[0])
for i in sorted(a):
    print(i.split()[2]+' '+i.split()[1]+' '+i.split()[0])