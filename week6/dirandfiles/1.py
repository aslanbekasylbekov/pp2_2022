import os
path = os.getcwd()#tekushi put
words = os.listdir(path) #soderzhimoye
file = list()
dir = list()
for word in words:
    if os.path.isdir(os.path.join(path,word)):
        dir.append(word)
    elif not os.path.isdir(os.path.join(path,word)):
        file.append(word)
print(words)
print(file)
print(dir)