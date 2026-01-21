# Write a program which accepts one number and prints the reverse of that no.

def Reverse():
    No=int(input("Enter any no :"))
    rev=0

    if No<0:
        No=-No

    while No>0:
        digit=No%10       #get last digit      123%10=3    12%10=2     1%10=1
        rev=rev*10+digit  #                    0*10+3=3    3*10+2=32   32*10+1=321
        No=No//10         #remove last digit   123//10=12  12//2=1     1//10=0
    print(rev)
    
def main():
    
    Reverse()

if __name__=="__main__":
    main()