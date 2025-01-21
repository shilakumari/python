#Print C pattern
n=5
for i in range(n):
    if i==0 or i==n-1:
        print('*'*n)
    else:
        print('*')
print()

#Print triangle
for i in range(n):
    print('*'*(i+1))
print()

numbers = [5, 10, 15]
for num in numbers:
    # '_' is valid variable and not using it
    for _ in range(num//5):
        print(num, end=' ')
    print()

#Reverse list
numbers=[10,20,30,40]
reversed_list = []
for i in range(len(numbers)-1,-1,-1):
    reversed_list.append(numbers[i])
print(reversed_list)

