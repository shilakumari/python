from datetime import *

def validateCard(expiryDate):
    if expiryDate > datetime.now().date():
        print("Valid")
    else:
        print("Not valid")

validateCard(date(2028,9, 12))