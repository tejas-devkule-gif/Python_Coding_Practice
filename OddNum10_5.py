# Write a program which accepts one number and prints Odd numbers till that number.

def OddNum():
    Num=int(input("Enter Any Number : "))
    
    for i in range(1,Num+1,2):
        i=i%Num
        print(i)
    
def main():
    
    OddNum()

if __name__=="__main__":
    main()