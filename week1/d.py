n = int(input())
z = input()
if z == 'b':
    print(n * 1024)
elif z == 'k':
    c = int(input())
    ans="{:."+ str(c) + "f}"
    print(ans.format(n/1024))