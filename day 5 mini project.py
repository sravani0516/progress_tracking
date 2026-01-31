from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance   

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self.acc_no}")
        print(f"Account Holder : {self.name}")
        print(f"Balance        : ₹{self.__balance}")

    
    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):

    def calculate_interest(self):
        interest = self.get_balance() * 0.04
        print(f"Interest Added: ₹{interest}")



class CurrentAccount(Account):

    def calculate_interest(self):
        print("No interest for Current Account.")



def main():
    print("===== Welcome to Python Bank =====")

    print("\nChoose Account Type:")
    print("1. Savings Account")
    print("2. Current Account")

    acc_type = int(input("Enter choice: "))
    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))

    if acc_type == 1:
        account = SavingsAccount(acc_no, name, balance)
    else:
        account = CurrentAccount(acc_no, name, balance)

    while True:
        print("\n===== Banking Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Calculate Interest")
        print("5. Display Account Details")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)

        elif choice == 2:
            amt = float(input("Enter withdrawal amount: "))
            account.withdraw(amt)

        elif choice == 3:
            print("Current Balance: ₹", account.get_balance())

        elif choice == 4:
            account.calculate_interest()  

        elif choice == 5:
            account.display_details()

        elif choice == 6:
            print("Thank you for using Python Bank!")
            break

        else:
            print("Invalid choice. Try again.")



main()
