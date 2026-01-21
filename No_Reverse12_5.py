# Write a program which accepts one number and prints that many numbers in reverse order.

def Display():
    num=int(input("Enter any no :"))

    for i in range(num,0,-1):
        print(i)
    
def main():
    Display()

if __name__=="__main__":
    main()