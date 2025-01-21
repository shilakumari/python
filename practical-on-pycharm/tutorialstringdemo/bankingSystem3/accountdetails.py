import os

ACCOUNT_FILE="accounts.txt"

def load_accounts_details():
    account_details=[]
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE,"r") as f:
            for line in f:
                account_number, name, password, balance = line.strip().split(",")
                account_details.append({
                    "account_number":account_number,
                    "name":name.strip(),
                    "password":password.strip(),
                    "balance":balance
                })

    return account_details[1:]#at 0 index is header
print(load_accounts_details())
