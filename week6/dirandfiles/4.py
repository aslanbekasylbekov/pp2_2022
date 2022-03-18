file = open("txt","r")
cnt = 0
x = file.read()
List = x.split("\n")
for i in List:
    if i:
        cnt += 1
print(cnt)