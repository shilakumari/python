class OverTheLimitException(Exception):
    def __init__(self,msg):
        self.msg=msg

def withdrawl(amount):
    if(amount>500):
        raise OverTheLimitException("You can not withdraw more than 500$ per day")
    else:
        print("You have withdraw %d"%amount)

withdrawl(300)
#withdrawl(550)
