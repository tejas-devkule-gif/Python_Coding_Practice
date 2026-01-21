# Write a program which accepts one number and prints that many numbers starting from 1.

def Display():
    Num=int(input("Enter any number :"))
    for i in range(1,Num+1):
        print(i)
    
def main():
    Display()

if __name__=="__main__":
    main()