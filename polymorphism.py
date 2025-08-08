class Calc:
    def multiply(self,a=0,b=1, *args):
        result = a*b
        for num in args:
            result *= num
        return result

calcu = Calc()

print(calcu.multiply())
print(calcu.multiply(2,3,4))

