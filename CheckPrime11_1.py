# Write a program which accepts one number and checks whether it is prime or not.
def CheckPrime():
    Num=int(input("Enter any number : "))
    count=0

    for i in range(1,Num+1):
        if(Num%i==0):        # if num%i==0 then True Eg num=5, i=1,2,3,4,5, divide 5 by 1 2 3 4 5, if 5%1==0 then true 
            count=count+1    #if true increment count by 1
    
    if(count==2):            #accept number which hat only count 2
        print("Prime No")
    else:
        print("Not prime")
    
def main():
    CheckPrime()

if __name__=="__main__":
    main()