n = int(input())
dem, hun = {}, {}
for i in range(n):
    demon, weakness = input().split()
    if weakness in dem:
        dem[weakness] += 1
    else:
        dem[weakness] = 1
m = int(input())
res = 0
for i in range(m):
    hunter, weakness, number = input().split()
    if weakness in hun:
        hun[weakness] += int(number)
    else:
        hun[weakness] = int(number)
for weakness in dem:
    if not weakness in hun:
        res += dem[weakness]
    elif weakness in hun and dem[weakness] - hun[weakness] >= 0:
        res += dem[weakness] - hun[weakness]
print('Demons left:',res)