# Write a program which accepts one number and prints binary equivalent.

def BinaryEquivalent_No(num):
    Binary=""  # empty string to store binary no

    while num>0:
        Binary=str(num%2)+Binary  # num%2 gives remainder (0/1) when div by 2 (binary digit)
        num=num//2 # This line divides the number by 2 and keeps only the whole number

    print("Binary equivalent is :",Binary)
    

def main():
    No=int(input("Enter any number :"))

    Ret=BinaryEquivalent_No(No)

if __name__=="__main__":
    main()