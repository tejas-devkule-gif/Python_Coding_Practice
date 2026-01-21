# Write a program which accepts one number and prints square of that number.
def SquareRoot():
    Num=int(input("Enter any number : "))
    
    for i in range(Num):
        i=Num*Num
    return i

def main():
    
    print("The square root of given number is :",SquareRoot())

if __name__=="__main__":
    main()