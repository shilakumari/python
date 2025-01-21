from accountdetails import load_accounts_details
from datetime import date


ACCOUNT_FILE="accounts.txt"

#Finding "account number" and "password" in key-value pair
accnos=[]
pwds=[]
balances=[]
acc_details=load_accounts_details()
for data in acc_details:
    for key,value in data.items():
        if key=="account_number":
            accnos.append(data[key])
        if key == "password":
            pwds.append(data[key])
        if key=="balance":
            balances.append(data[key])
n=len(accnos)
#Account Number and password
accno_pwds={}
for i in range(n):
    accno_pwds[accnos[i]]=pwds[i]
#print(accno_pwds)

#Account Number and balance
accno_balances={}
for i in range(n):
    accno_balances[accnos[i]]=balances[i]
#print(accno_balances)

is_valid=False
entered_account=0
#Account Login
def acc_login():
    global is_valid
    global entered_account
    is_valid=False
    acc_no=input("Enter your account number:")
    entered_account = acc_no
    if acc_no in accno_pwds.keys():
        #print(acc_no)
        pwd = input("Enter your password:")
        if accno_pwds[acc_no]==pwd:
            is_valid=True
    return is_valid

#print(acc_login())
#print(is_valid)

"""
#Performing transaction (Deposit/Withdrawal)
def acc_transactions():
    while is_valid:
        acc_no = entered_account
        t_type= input("Transaction Type (Deposit/Withdrawal):")
        if t_type=="Deposit":
            amount = int(input("Enter Amount:").strip())
            final_amount=0
            for data in acc_details:
                if data["account_number"] == str(acc_no):
                    final_amount = int(data["balance"]) + amount
                    data["balance"] = str(final_amount)
                print(data)
            print(acc_no, t_type, final_amount, date)
        elif t_type=="Withdrawal":
            amount = input("Enter Amount:")
        else:
            print("Invalid Type")

"""

