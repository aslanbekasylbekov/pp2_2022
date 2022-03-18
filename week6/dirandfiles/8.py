import os
file = 'C:\PP2\week6\dirandfiles\copy.txt'
if os.access(file,os.F_OK):
    os.remove(file)