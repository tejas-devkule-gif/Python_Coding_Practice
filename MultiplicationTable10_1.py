# Write a program which accepts one number and prints multiplication table of that number.

def Multiply():
    Num=int(input("Enter Any Number : "))
    Ans=0
    for i in range(1,11):
        Ans=Num*i
        print(Ans)
    
def main():
    
    Multiply()

if __name__=="__main__":
    main()