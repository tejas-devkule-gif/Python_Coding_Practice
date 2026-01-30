def CheckPrime(Num):

    if Num<=1:
        return False
    
    for i in range(2,Num):
        if(Num%i==0):        # if num%i==0 then True for example num=5, i=1,2,3,4,5, divide 5 by 1 2 3 4 5, if 5%1==0 then true 
           return False
        return True

def main():
    num=int(input("Enter number :"))
    Ret=CheckPrime(num)

    if Ret==True:
        print("It is prime no")
    else:
        print("Not prime")

if __name__=="__main__":
    main()