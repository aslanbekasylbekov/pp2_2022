from itertools import permutations
def per(s):
    perms = [''.join(p) for p in permutations(s)]
    print(perms)
s = input()
per(s)