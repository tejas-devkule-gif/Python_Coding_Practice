def factorial():
    Num=int(input("Enter Number : "))
    temp=1
    for i in range(1,Num+1):
        temp=temp*i
    print("factorial No is : ",temp)

factorial()