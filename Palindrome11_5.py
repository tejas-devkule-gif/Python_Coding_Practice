# Write a program which accepts one number and check whether the no is palindrome or not.

def Palindrome():
    No=int(input("Enter any no :"))
    temp=No
    rev=0

    if temp<0:
        temp=-temp

    while temp>0:
        digit=temp%10       #get last digit      123%10=3    12%10=2     1%10=1
        rev=rev*10+digit    #                    0*10+3=3    3*10+2=32   32*10+1=321
        temp=temp//10       #remove last digit   123//10=12  12//2=1     1//10=0

    if(No==rev):
        print("no is palindrome")
    else:
        print("No is not palindrome")
    
def main():
    
    Palindrome()

if __name__=="__main__":
    main()