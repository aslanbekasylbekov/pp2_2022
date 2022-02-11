num = input()
num = list(map(int,num.split()))
jump = 0
i = 0
while i <= jump and i < len(num)-1:
    if jump >= len(num)-1:
        break
    else:
        jump = max(jump,i+num[i])
    i += 1
if jump >= len(num)-1:
    print("1")
else:
    print("0")

