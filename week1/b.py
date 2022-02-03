n=str(input())
summ=0
for i in n:
    summ+=ord(i)
if summ>300:
    print("It is tasty!")
else:
    print("Oh, no!")   
