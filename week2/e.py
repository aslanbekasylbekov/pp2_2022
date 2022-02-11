n = list(map(int, input().split()))
x = None
if len(n) <= 1:
    x = int(input())
if x is None:
    x = n[1]
n = n[0]
arr = []
summ = 0
for i in range(0,n):
    arr.append(x + 2*i)
    summ ^=arr[i]
print(summ)