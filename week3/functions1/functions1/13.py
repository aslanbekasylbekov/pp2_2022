def check(n,lucky):
    if n==lucky:
        print("Good job, KBTU! You guessed my number in " + str(cnt) + " guesses!")
        return True
    else:
        print("Your guess is too low.")
        return False

name = input("Hello! What is your name?")
print("Well, " + name + " в, I am thinking of a number between 1 and 20.")
print("Take a guess.")
lucky = 19
cnt = 0
while True:
    n=int(input())
    if check(n,lucky)== True:
        break
    print("Take a guess.")