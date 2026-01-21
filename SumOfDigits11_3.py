# Write a program which accepts one number and prints sum of digits.

def Sum_No():
    No=int(input("Enter any number : "))
    sum=0

    if  No<0:
        No=-No

    while No>0:
        digit=No%10      #gets last digit            123%10=3    12%10=2    1%10=1
        sum=sum+digit    #add/assign digit to summ   0+3=3       3+2=5      5+1=6
        No=No//10        #remove last digit          123//10=12  12//10=1   1//10=0  until no=0
    print(sum)                                     #sum=6
       
def main():
    
    Sum_No()

if __name__=="__main__":
    main()