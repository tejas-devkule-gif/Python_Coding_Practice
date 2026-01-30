def AddFactorial():
    Num=int(input("Enter Number : "))
    for i in range(1,Num+1):
            if Num%i==0:
                print(i,end=" + ")
                add=i+i
    print(add)

AddFactorial()