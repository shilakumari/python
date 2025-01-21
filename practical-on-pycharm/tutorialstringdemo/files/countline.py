f=open('sample.txt','r')
#print(len(f.readlines()))
#split the content with newline and count
print(len(f.read().split('\n')))