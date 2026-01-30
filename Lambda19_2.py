Power=lambda No1,No2 : No1 * No2

def Main():
    no1=int(input("Enter first number :"))
    no2=int(input("Enter second number :"))
    Ret = Power(no1,no2)
    print(Ret)

if __name__=="__main__":
    Main()