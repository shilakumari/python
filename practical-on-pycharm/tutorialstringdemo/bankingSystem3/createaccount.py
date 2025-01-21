import random

ACCOUNT_FILE="accounts.txt"
def create_account():
    name= input("Enter your name:")
    initial_deposit=int(input("Enter your initial deposit:"))
    account_num = ""
    for i in range(15):
        account_num += str(random.randint(0, 9))
    pwd = input("Enter a password:")

    details= ",".join([str(account_num), str(name), str(pwd), str(initial_deposit)])
    with open(ACCOUNT_FILE, "a") as f:
        f.write(f"{details}\n")
    print("Account created successfully!")
    print("(Account details saved to accounts.txt)")
