n = int(input())
a =[]
for i in range(n):
    upper, lower, num = 0, 0, 0
    password = input()
    if password in a:
        continue
    else:
        for x in password: 
            if ord(x) >= 65 and ord(x) <= 90:
                upper += 1
            elif  ord(x) >= 97 and ord(x) <= 122:
                lower += 1
            elif ord(x) >= 48 and ord(x) <= 57:
                num += 1
        if upper > 0 and lower > 0 and num > 0: 
            a.append(password) 
a.sort() 
print(len(a))
print(*a,sep='\n')