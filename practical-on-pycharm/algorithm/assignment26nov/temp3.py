#value="11 34 67 89"
value = input()
l = value.split()
for i in l:
  if i.isdigit():
    j = int(i)
    print(j+1)