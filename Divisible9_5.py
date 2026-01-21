# Write a program which accepts one number and checks whether it is divisible by 3 and 5

def Divisible():
    Num=int(input("Enter any number : "))
    
    if (Num%3==0 and Num%5==0):
        print("The number is divisible by 3 and 5")
    else:
        print("The number is not divisible by 3 and 5")

def main():
    
    Divisible()

if __name__=="__main__":
    main()