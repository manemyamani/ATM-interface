import time
from datetime import datetime

userid = 'yamini'
password = 6117

user = input("Please insert Your user id: ")
pin = int(input("Enter your ATM pin: "))

balance = 5000
transaction_history = []

if pin == password and userid == user:
    while True:
        print("""
              
              ********Menu********
              """
              )
        print(""" 
            1 == Transactions history
            2 == Withdraw balance
            3 == Deposit balance
            4 == Transfer
            5 == Exit
            """
              )

        try:    
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue
        
        if option == 1:
            print("===========================================================================================================")
            print("===========================================================================================================")
            print("Your transactions history:")
            for transaction in transaction_history:
                print(transaction)
            print("===========================================================================================================")
            print("===========================================================================================================")
                                     
        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                transaction_history.append(f"{timestamp}   Debited: {withdraw_amount}   Balance: {balance}")
                print("===========================================================================================================")
                print("===========================================================================================================")
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {balance}")
            else:
                print("Insufficient balance!")
            print("===========================================================================================================")
            print("===========================================================================================================")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_history.append(f"{timestamp}   Credited: {deposit_amount}   Balance: {balance}")
            print("===========================================================================================================")
            print("===========================================================================================================")
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")
            print("===========================================================================================================")
            print("===========================================================================================================")

        elif option == 4:
            transfer_amount = int(input("Please enter transfer amount: "))
            if transfer_amount <= balance:
                recipient = input("Please enter recipient account: ")
                balance -= transfer_amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                transaction_history.append(f"{timestamp}  Transferred: {transfer_amount} to {recipient}    Balance: {balance}")
                print("===========================================================================================================")
                print("===========================================================================================================")
                print(f"{transfer_amount} is transferred to {recipient}")
                print(f"Your updated balance is {balance}")
            else:
                print("Insufficient balance!")
            print("===========================================================================================================")
            print("===========================================================================================================")

        elif option == 5:
            break

        else:
            print("Invalid option, please try again.")
else:
    print("Wrong pin or wrong userid! Please try again")
