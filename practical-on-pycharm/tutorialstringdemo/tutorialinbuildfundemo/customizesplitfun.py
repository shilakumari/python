class MyStr:
    def __init__(self, s, delimiter):
        self.s=s
        self.mylist=[]
        self.delimiter = delimiter
    def mysplit(self):
        temp = ""
        for letter in self.s:
            if letter == self.delimiter:
                self.mylist.append(temp)
                temp = ""
            else:
                temp += letter
        #at last time temp, add to mylist
        self.mylist.append(temp)

obj = MyStr("Hello Worldly People"," ")
obj.mysplit()
print(obj.mylist) #['Hello', 'Worldly', 'People']
