import os
import time
class BankAccount:
    def __init__ (self, balance=0):
        self.balance=float(balance)

    def deposite(self, amount):
        self.balance +=amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -=amount
            print(f"Withdraw: {amount}")


    def show(self):
        print(f"Total balance {self.balance}\n ")    

balance =float(input("Enter Initial Balance: "))
account=BankAccount(balance)

while True: 
    print("\n =====Bank Menu===== ")
    print("1. Check Balance")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Exit")


    choice=int(input("Ente your choice(1-4): "))

    if choice == 1:
        account.show()
    elif choice == 2:
        amt=float(input("Enter amount to deposit: "))
        account.deposite(amt)   
    elif choice == 3:
        amt=float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice ==4:
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice, please try again.")   
        time.sleep(3)     

        os.system("cls" if os.name =="nt" else "clear")