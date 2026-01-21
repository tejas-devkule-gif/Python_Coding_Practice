# Write a program which accepts one number and prints count of digit in that number.

def Count_No():
    Num=int(input("Enter any number : "))
    count=0
    temp=Num

    if temp==0:  #handles 0 and negative nos
        count=1
    else:
        if temp<0:
            temp=-temp #make no positive
        while temp>0:
            temp=temp//10  #eg 3//10=3.33 floor division=3
            count=count+1
    print("No of digits are :",count) 
       
def main():
    Count_No()

if __name__=="__main__":
    main()