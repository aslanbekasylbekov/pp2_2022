def has_33(n):
    for i in range(len(n)-2):
        if n[i]==n[i+1]==0 and n[i+2]==7:
            return True
    return False
n = list(map(int,input().split()))
if has_33(n)==True:
    print("True")
else:
    print("False")