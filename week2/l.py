s = input()
stack = []
res = True
for i in s:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            res = False
            break
        open_bracket = stack.pop()
        if open_bracket=='(' and i == ')':
            continue
        if open_bracket=='[' and i == ']':
            continue
        if open_bracket=='{' and i == '}':
            continue
        res = False
        break
if res and len(stack)==0:
    print('Yes')
else:
    print('No')