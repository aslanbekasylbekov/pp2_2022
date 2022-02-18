def histogram(s):
    for i in s:
        for x in range(i):
            print('*',end='')
        print()
s = list(map(int,input().split()))
histogram(s)