# Write a program which contains one function chkGreater() that accepts two numbers and print the greater number.
def cheackGreater():
    
    No1=int(input("Enter 1st number : "))
    No2=int(input("Enter 2nd number : "))

    if(No1>No2):
        print("No1 is greater then No2")
    else:
        print("No2 is greater than No1")


def main():
    cheackGreater()

if __name__=="__main__":
    main()