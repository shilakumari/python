"""size=4
arr = [11, 21, 31, 41 ]
#rev = arr[::-1]
for i in range(size-1,-1,-1):
    print(arr[i], end=' ')
print("&&&&&")

location = size-1
while location>=0:
    print(arr[location])
    location -= 1
#print binary triangle
for i in range(1, 6):
    for j in range(1, i+1):
        if j%2==0:
            print("0",end=' ')
        else:
            print("1",end=' ')
    print()
#print Z shape
for i in range(5,0, -1):
    for j in range(1,6):
        if i==1 or i==5:
            print("*",end='')
        else:
            if i==j:
                print("*",end='')
            else:
                print(" ", end='')
    print()"""
#String examples
print("Python"[0])
str="Python, World"
price=20
print(str.lower())
print(str[-1])
print(str[1:4])
print(str.split())
print(f"the price is {price}")
print("Py".upper())


