s = input()
n = len(s)
def dec(s, i, ans):
    if i == n:
        print(ans)
        return 
    ans += int(s[i]) * (2 ** (n - 1 - i))
    return dec(s, i + 1, ans)
dec(s, 0, 0)
