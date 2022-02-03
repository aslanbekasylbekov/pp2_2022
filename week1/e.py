n,f = map(int, input().split()) 
prime = True
if (n > 1): 
    for i in range(2,n): 
        if n % i == 0: 
            prime = False 
            break 
if (n < 500 and  prime and f % 2 == 0): 
    print("Good job!") 
else: 
    print("Try next time!")