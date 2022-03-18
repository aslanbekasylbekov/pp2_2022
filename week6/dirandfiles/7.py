file = open('inform.txt','r')
with open('copy.txt','w') as f:
    for i in file:
        f.write(i+ ' ')