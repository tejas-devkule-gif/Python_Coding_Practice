# Write a program which contains one function named as ChkNum() 
# which accepts one parameter as number.If number is even then it should display "Even number" otherwise display "Odd number" on console.

def Chknum(no):

    if (no%2==0):
        print("Even Number :",no)
    else:
        print("Odd Number :",no)
    
def main():
    num=int(input("Enter any number :"))

    Ret=Chknum(num)


if __name__=="__main__":
    main()