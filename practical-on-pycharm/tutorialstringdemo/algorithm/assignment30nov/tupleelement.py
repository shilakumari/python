tuple1=(10,9,8,7,6,5)
element_to_check=9

is_present=False
for ele in tuple1:
    if ele==element_to_check:
        is_present=True

if is_present:
    print(True)
else:
    print(False)