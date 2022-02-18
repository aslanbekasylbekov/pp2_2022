class Account:
    owner = ''
    balance = 0
    def __init__(self, a): #when creating account in bank, balance is 0
        self.owner = a
    def deposit(self, s):
        if self.balance + s>1000000:
            print("OVerload")
        else:
            self.balance+=s
        self.balance += s
    def withdraw(self, s):
        if s > self.balance:
            print("Sorry, not enough funds")
        else:
            self.balance -= s
    def str(self):
        return self.owner, self.balance
    def sb(self):
        if self.balance == 1:
            print("You balance is", self.balance, "tenge")
        elif self.balance == 0:
            print("You do not have any funds")
        else:
            print("You balance is", self.balance, "tenge")
a1 = Account(input("Enter your name: "))
while True:
    print("What do you want to do: ")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Selfbalance")
    print()
    print()
    print("If you want to finish,press '4' ")
    ch=int(input()) 
    if ch==1:
        d=int(input())
        a1.deposit(d)
        print()
    if ch==2:
        w=int(input())
        a1.withdraw(w)
        print()
    if ch==3:
        a1.sb()
        print()
    if ch==4:
        break