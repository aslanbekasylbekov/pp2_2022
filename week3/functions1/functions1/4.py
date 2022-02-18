def prime(n):
    prime = True
    answer = list()
    for i in n:
        if i<2:
            prime = False        
        for x in range(2,i):
            if i % x == 0:
                prime=False
                break
        if prime == True:
            answer.append(i)
        prime = True
    return answer
n = list(map(int,input().split()))
print(*prime(n))