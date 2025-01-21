print(5&3)#1
print(5|3)#7
print(5^3)#6
print(~5)#-6
print(bin(64))
print(int(0b1000000))

a=15 #1111
#print(bin(~a)) #-0b10000
print(~a & 0b1111) #0

"""
ar=[1,2,1]
k1=2
def check_subset_exists(arr,k):
    count_dict = {}
    for num in arr:
        count_dict[num]=count_dict.get(num,0)+1
    for num,count in count_dict.items():
        if count>=k:
            print("True")
            return
    print("False")

check_subset_exists(ar,k1)
"""
