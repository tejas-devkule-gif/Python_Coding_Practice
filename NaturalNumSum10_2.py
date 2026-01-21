# Write a program which accepts one number and prints sum of first n natural numbers.

def NaturalNumSum():
    Num=int(input("Enter Any Number : "))
    Sum=0
    for i in range(1,Num+1):
        Sum=Sum+i
    print("Sum of n natural no is : ",Sum)
    
def main():
    
    NaturalNumSum()

if __name__=="__main__":
    main()