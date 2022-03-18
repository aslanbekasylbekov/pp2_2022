def palindrome(s):
    isPalin = True
    for i in range(0,int(len(s)/2)):
        if s[i]!=s[len(s)-i-1]:
            isPalin = False
    return isPalin
s = input()
if palindrome(s):
    print('Yes')
else:
    print('No')