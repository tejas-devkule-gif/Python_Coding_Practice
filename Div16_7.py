# Write a program which accept number from user 
# and cheak whether that number is divisible by 5 otherwise return false.

def Divisible(no):

    if (no%5==0):
        print("This number is divisible by 5")
    else:
        print("Not divisible")


def main():

    no=int(input("Enter any number :"))

    Ret=Divisible(no)

if __name__=="__main__":
    main()