n = int(input())
dict = {}
for i in range(n): 
    name, sum = map(str, input().split()) 
    sum = int(sum)
    if name in dict.keys():
        dict[name] += sum
    else:
        dict[name] = sum
new_value = list(dict.values()) 
new_name = list(dict.keys()) 
new_value.sort()
new_name.sort()
max = new_value[len(new_value)- 1]
for name in new_name:
    if max - dict[name] == 0:
        print(name, "is lucky!")
    else:
        print(name, "has to receive",max - dict[name],"tenge")