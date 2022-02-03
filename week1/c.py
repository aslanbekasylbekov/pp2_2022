def lower_case(x):
    for i in x:
        print(chr(ord(i) + 32), end='') if 65 <= ord(i) <= 90 else print(i, end='')
x = input()
lower_case(x)