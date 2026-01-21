# Write a program which accepts one number and prints factorial of that number.

def Factorial():
    Num=int(input("Enter Any Number : "))
    fact=1
    for i in range(1,Num+1):
        fact=fact*i
        print("factorial of no is : ",fact)
    
def main():
    
    Factorial()

if __name__=="__main__":
    main()