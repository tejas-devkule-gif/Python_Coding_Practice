# Write a program which accepts one number and prints even numbers till that number.

def EvenNum():
    Num=int(input("Enter Any Number : "))
    
    for i in range(2,Num+1,2):
        i=i%Num
        print(i)
    
def main():
    
    EvenNum()

if __name__=="__main__":
    main()