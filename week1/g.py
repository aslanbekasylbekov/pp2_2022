n = input()
summ = 0
for i in range(0,len(n)):
    summ += int(n[i])*(2**(len(n)-i))//2
print(summ)