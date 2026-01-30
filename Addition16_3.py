# Write a program which contains one function named as Add()
# which accepts two parameters as number and return addition of that two numbers.

def Add(No1,No2):

    Ans=0
    Ans=No1+No2
    print("Addition is :",Ans)

def main():

    no1=int(input("Enter first Number :"))
    no2=int(input("Enter second number :"))

    Ret=Add(no1,no2)

if __name__=="__main__":
    main()