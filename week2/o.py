dict = ['ZER', 'ONE', 'TWO', 'THR', 'FOU', 'FIV', 'SIX', 'SEV', 'EIG', 'NIN']
def stringTonumber(s):
    res = ''
    for i in range(0, len(s), 3):
        numberindinct = s[i] + s[i+1] + s[i+2]
        res += str(dict.index(numberindinct))
    return res
a, b = input().split('+')
sum = int(stringTonumber(a)) + int(stringTonumber(b))
for i in str(sum):
    print(dict[int(i)], end='')