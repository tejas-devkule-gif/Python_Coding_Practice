# Write a program which accepts two numbers and prints addition, subtraction, multiplication, and division
Ans=0
def Add(No1,No2):
    Ans=No1+No2
    print("Addition is :",Ans)

def Sub(No1,No2):
    Ans=No1-No2
    print("Subtraction is :",Ans)

def Div(No1,No2):
    Ans=No1/No2
    print("Division is :",Ans)

def main():
    No1=int(input("Enter 1st no :"))
    No2=int(input("Enter 2nd no :"))
    Add(No1,No2)
    Sub(No1,No2)
    Div(No1,No2)

if __name__=="__main__":
    main()