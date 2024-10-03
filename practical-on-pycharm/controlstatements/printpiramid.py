n=int(input("Enter number to print pyramid"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)
