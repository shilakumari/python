import accountlogin
from accountdetails import load_accounts_details
from accountlogin import acc_login
from createaccount import create_account

from transactions import acc_transactions

ACCOUNT_FILE="accounts.txt"

def main():
    while True:
        print("Welcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        if choice=="1":
            create_account()
        elif choice=="2":
            is_valid=acc_login()
            entered_acc = accountlogin.entered_account
            if is_valid:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice=="1":
                        deposit(entered_acc,is_valid)
                    elif sub_choice=="2":
                        withdraw(entered_acc,is_valid)
                    elif sub_choice=="3":
                        print("Logged out successfully.")
                        break
                #print(is_valid)
                #print(entered_acc)
            else:
                print("Invalid account number or password.")

            #acc_transactions()
            #print(transactions.final_data)

        elif choice=="3":
            print("Exit")
            val=load_accounts_details()
            print(val)
            break
        else:
            print("Invalid choice! please try again")

if __name__=="__main__":
    main()