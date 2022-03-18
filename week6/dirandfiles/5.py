file = open("new.txt","w")
x = list(map(str,input().split()))
for i in x:
    file.write(i + " ")