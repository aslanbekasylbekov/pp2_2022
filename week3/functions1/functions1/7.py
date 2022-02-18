def has_33(n):
    for i in range(len(n)-1):
        if n[i]==n[i+1]==3:
            return True
    return False
n = list(map(int,input().split()))
if has_33(n)==True:
    print("True")
else:
    print("False")