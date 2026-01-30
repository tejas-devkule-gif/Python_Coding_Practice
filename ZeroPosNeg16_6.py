# write a program which accept number from user and cheak that number is positiove , negative or zero.

def ChkNum(num):
    
    if num==0:
        print("It is zero number")
    elif num>0:
        print("Positive number")
    else:
        print("Negative number")


def main():

    num=int(input("Enter any number :"))
    Ret=ChkNum(num)

if __name__=="__main__":
    main()