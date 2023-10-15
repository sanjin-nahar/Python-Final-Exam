import random
 
 
class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.users = []
        self.total_balance = 0
        self.total_loan = 0
        self.bankrupt = False
        self.loan_system = True
 
 
class User:
    def __init__(self, name, email, address, account_type, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
        self.balance = 0
        self.account_no = random.randint(500, 5000)
        self.transaction_history = []
        self.loan_times = 0
 
    def password(self, password):
        self.password = password
 
    def deposite(self, bank, amount):
        if bank.bankrupt == False:
            if amount > 0:
                self.bank = bank
                self.balance += amount
                self.bank.total_balance += amount
                history = f"Successfully deposited: ${amount}. New Balance: ${self.balance}"
                self.transaction_history.append(history)
                print(history)
            else:
                print(f"Invalid deposit amount. Please Try again!")
        else:
            print("The bank is bankrupt, you cann't deposit money")
 
    def withdraw(self, bank, amount):
        if bank.bankrupt == False:
            if amount > 0 and amount <= self.balance:
                self.bank = bank
                self.balance -= amount
                self.bank.total_balance -= amount
                history = f"Withdraw: ${amount}. New Balance: ${self.balance}"
                self.transaction_history.append(history)
                print(history)
            elif amount > self.balance:
                print(f"Withdrawal amount exceeded")
            else:
                print(f"Invalid amount request. Please Try again!")
        else:
            print(f"The bank is bankrupt, you cann't withdraw money")
 
    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
 
    def transaction_history(self):
        if len(self.transaction_history) > 0:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("There is no transaction history.")
 
    def loan(self, bank, amount):
        self.bank = bank
        if self.bank.bankrupt == False:
            if self.bank.loan_system == True:
                if self.loan_times <= 2:
                    self.balance += amount
                    self.bank.total_balance -= amount
                    self.bank.total_loan += amount
                    history = f"Loan issued successfully and ${amount} added"
                    self.transaction_history.append(history)
                    self.loan_times += 1
                    print(history)
                else:
                    print("Sorry! You have already taken the maximum number of loan 2.")
            else:
                print(f"The bank loan system is turned off")
        else:
            print(f"The bank is bankrupt, you cann't take loan")
 
    def transfer(self, bank, amount, user_name):
        self.bank = bank
        if len(self.bank.users) >= 2:
            for user in self.bank.users:
                if user_name == user.name:
                    if self.balance >= amount:
                        user.balance += amount
                        self.balance -= amount
                        history = f"Balance successfully transferred to {user_name} from {self.name}, and the amount is {amount}"
                        self.transaction_history.append(history)
                        print(history)
                        return
                    else:
                        print(f"Transaction amount exceed")
                        return
            else:
                print(f"Username {user_name} doesn't exists.")
        else:
            print(f"There are few user.")
 
 
class Admin:
    def __init__(self, bank) -> None:
        self.bank = bank
        self.name = "sanjin"
        self.password = "12345678"
 
    def show_users(self):
        if len(self.bank.users) > 0:
            print(f"Available users down below")
            for user in self.bank.users:
                print(
                    f"Name: {user.name}, Account No: {user.account_no}, Email: {user.email}, Address: {user.address}, Account Type: {user.account_type}"
                )
                print()
        else:
            print(f"No user found.")
 
    def check_bank_balance(self):
        print(
            f"Total balance of {self.bank.name} bank is ${self.bank.total_balance}"
        )
 
    def check_bank_loan(self):
        print(
            f"Total loan of {self.bank.name} bank is ${self.bank.total_loan}")
 
    def loan_system_status(self, status):
        if status == "1":
            self.bank.loan_system = True
            print(f"The loan system is turned on!")
        elif status == "2":
            self.bank.loan_system = False
            print(f"The loan system is turned off!")
        else:
            print(f"Invalid key status. Please try again!")
 
    def bankrupt_status(self, status):
        if status == "1":
            self.bank.bankrupt = True
            print(
                f"{self.bank.name} bank successfully bankrupted by the admin")
        elif status == "2":
            self.bank.bankrupt = False
            print(f"{self.bank.name} is successfully opened by admin!")
        else:
            print(f"Invalid key status. Please try again!")
 
    def delete_user(self, email):
        for user in self.bank.users:
            if user.email == email:
                self.bank.users.remove(user)
                print(f"{user.name} deleted successfully")
                return
        print("User not found!")
 
 
class Authentication:
    def __init__(self) -> None:
        self.logged_in = None
 
    def Registration(self, bank, user):
        self.bank = bank
        self.user = user
        for users in bank.users:
            if self.user.email == users.email:
                print(f"Already Registered!")
                return
        self.bank.users.append(self.user)
        print(f"{self.user.name} registered successfully!")
 
    def login(self, bank, email, password):
        self.bank = bank
        for user in self.bank.users:
            if user.email == email and user.password == password:
                self.logged_in = user
                print(f"{user.name} successfully logged in!")
                return True
        print("Invalid email or password. Please try agian!")
 
    def log_out(self):
        self.logged_in = None
 
 
brac = Bank("brac", "Dhaka")
admin = Admin(brac)
register = Authentication()
 
while True:
    print(f"Welcome to the {brac.name} bank")
    print("Log in Admin User as admin and password - 12345678")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    option = input("Enter option:")
 
    if option == "1":
        print("Login as Admin")
        user_name = input("Enter admin name:")
        password = input("Enter admin password:")
        if user_name == admin.name and password == admin.password:
            print("Successfully logged in")
            while True:
                print("1. Create account for user")
                print("2. Show all user accounts")
                print("3. Show total available balance")
                print("4. Show total loan amount")
                print("5. Delete user account")
                print("6. Turn on/off loan system")
                print("7. Turn on/off bankrupt system")
                print("8. Log Out")
                option = input("Enter option:")
 
                if option == "1":
                    name = input("Enter user name:")
                    email = input("Enter user email:")
                    address = input("Enter user address:")
                    account_type = input(
                        "Enter '1' for 'Savings' type or Enter '2' for 'Current' type account: "
                    )
                    password = input("enter user password:")
                    if account_type == "1":
                        new_user = User(name, email, address,
                                        "Savings", password)
                    elif account_type == "2":
                        new_user = User(name, email, address,
                                        "Current", password)
                    else:
                        print("Invalid account type. Please Try again!")
                    register.Registration(brac, new_user)
                elif option == "2":
                    admin.show_users()
                elif option == "3":
                    admin.check_bank_balance()
                elif option == "4":
                    admin.check_bank_loan()
                elif option == "5":
                    email = input("Enter email:")
                    admin.delete_user(email)
                elif option == "6":
                    option = input(
                        "Enter '1' for 'turned on' or Enter '2' for 'turned off':"
                    )
                    admin.loan_system_status(option)
                elif option == "7":
                    option = input(
                        "Enter '1' for 'turned on' or Enter '2' for 'turned off':"
                    )
                    admin.bankrupt_status(option)
                elif option == "8":
                    break
                else:
                    print("Invalid selection. Please try again!")
        else:
            print("Invalid name or password. Please Try again!")
    elif option == "2":
        if len(brac.users) > 0:
            print("Login as User")
            user_email = input("Enter user email:")
            password = input("Enter password:")
            log_in = register.login(brac, user_email, password)
            if log_in:
                while True:
                    print("1. Show Balance")
                    print("2. Deposite Money")
                    print("3. Withdraw Money")
                    print("4. Transfer Money")
                    print("5. Transaction History")
                    print("6. Take Loan")
                    print("7. Log Out")
                    option = input("Enter Option:")
                    user = register.logged_in
 
                    if option == "1":
                        user.show_balance()
                    elif option == "2":
                        amount = int(input("Enter amount:"))
                        user.deposite(brac, amount)
                    elif option == "3":
                        amount = int(input("Enter amount:"))
                        user.withdraw(brac, amount)
                    elif option == "4":
                        name = input("Enter name of receiver:")
                        amount = int(input("Enter amount:"))
                        user.transfer_money(brac, amount, name)
                    elif option == "5":
                        user.show_transaction_history()
                    elif option == "6":
                        amount = int(input("Enter loan amount:"))
                        user.take_loan(brac, amount)
                    elif option == "7":
                        register.log_out()
                        break
                    else:
                        print("Invalid options. Please Try again!")
            else:
                print("No Login User. Please Try again!")
        else:
            print("There are no user. Please contact with admin")
    elif option == "3":
        break
    else:
        print("Invalid option. Please Try again!")
