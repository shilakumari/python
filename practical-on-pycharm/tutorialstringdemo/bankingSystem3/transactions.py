import accountlogin
from accountdetails import load_accounts_details
#from accountlogin import acc_login
from datetime import date

#final_data=[]
#is_valid=accountlogin.acc_login()
#entered_acc = accountlogin.entered_account

TRANSACTIONS_FILE="transactions.txt"
def log_transaction(entered_acc,transaction_type,amount):
    with open(TRANSACTIONS_FILE,"a") as f:
        dates = date.today()
        #print(dates)
        f.write(f"{entered_acc},{transaction_type},{amount},{dates}\n")

def deposit(entered_acc,is_valid):
    pass















def acc_transactions():
    is_valid=accountlogin.acc_login()
    entered_account = accountlogin.entered_account
    if is_valid:
        acc_details = load_accounts_details()
        print(is_valid,"Login Successful!")
        print(entered_account)
        while is_valid==True:
            acc_no = entered_account
            t_type = input("Transaction Type (Deposit/Withdrawal):").strip()
            if t_type == "Deposit":
                amount = int(input("Enter Amount:").strip())
                final_amount = 0
                for data in acc_details:
                    if data["account_number"] == str(acc_no):
                        final_amount = int(data["balance"]) + amount
                        data["balance"] = str(final_amount)
                    #final_data.append(data)
                    #print(data)
                dates=date.today()
                print(acc_no, t_type, final_amount, dates)

                break
            elif t_type == "Withdrawal":
                amount = input("Enter Amount:")
                break
            else:
                print("Invalid Type")
    else:
        print("Invalid account number or password")


#acc_transactions()
#print(final_data)