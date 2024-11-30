class MathUtils:
    @staticmethod
    def add(a, b=10):
        return a+b

    @staticmethod
    def multiply(a,b=2):
        return a*b

print(MathUtils.add(5,MathUtils.multiply(2))) #9

