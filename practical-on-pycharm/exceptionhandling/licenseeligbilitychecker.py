class TooYoungExceptionChecker(Exception):
    def __init__(self,msg):
        self.msg=msg

class TooOldExceptionChecker(Exception):
    def __init__(self,msg):
        self.msg=msg

age = int(input("Enter the age"))
if age < 18:
    raise TooYoungExceptionChecker("You have to be 18 or older to apply")
elif age >90:
    raise TooOldExceptionChecker("you have to be younger than 90")
else:
    print("You are eligible")
