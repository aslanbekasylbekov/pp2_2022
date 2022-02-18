def rev(s):
    answer = list()
    for i in range(len(s)):
        answer.append(s[len(s)-i-1])
    return answer
s = list(map(str,input().split()))
for i in rev(s):
    print(i,end=' ')