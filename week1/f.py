n = int(input())
for i in range(n):
    a = int(input())
    if 45<a:
        print("Burn! Burn! Burn Young!")
    elif 25<a<=45:
        print("Okay, fine")
    elif 10 < a or a==25:
        print("You are weak")
    elif a<=10:
        print("Go to work!")