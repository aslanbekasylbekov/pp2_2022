n = int(input())
for i in range(0,n):
    for j in range(0,n):
        if n%2==1:
            if i+j>=n-1:
                print('#',end='')
            else:
                print('.',end='')
        else:
            if i<j:
                print('.',end='')
            else:
                print('#',end='')
    print(end='\n')