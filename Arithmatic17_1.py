# create an module named as arithmatic which contains 4 functions as Add() for addition, Sub( for subtraction, Mul( for multiplication, Div() for diision. all function
# accepts two parameter as number and perform the operation. write on python program which calls all the functions from arithmatic module by accepting the two number from user.

import Arithmatic17_1 
def main():
    no1=int(input("Enter 1st num :"))
    no2=int(input("enter 2nd num :"))

def Add(No1,No2):
    print("Addition is :",No1+No2)
def Sub(No1,No2):
    print("Subtraction is :",No1-No2)
def Mult(No1,No2):
    print("Multiplication is :",No1*No2)
def Div(No1,No2):
    print("Division is :",No1/No2)
   
    Ret=Arithmatic17_1.Add(No1,No2)    
    Ret=Arithmatic17_1.Sub(No1,No2)
    Ret=Arithmatic17_1.Mult(No1,No2)
    Ret=Arithmatic17_1.Div(No1,No2)


if __name__=="__main__":
    main()