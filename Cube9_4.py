# Write a program which accepts one number and prints cube of that number.
def Cube():
    Num=int(input("Enter any number : "))
    
    for i in range(Num):
        i=Num*Num*Num
    return i

def main():
    
    print("The square root of given number is :",Cube())

if __name__=="__main__":
    main()