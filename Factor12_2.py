# Write a program which accepts one number and prints its factors.
def factor():
    No=int(input("Enter any character :"))

    for i in range(1,No+1):
        if No%i==0:
            print(i)

    

def main():
    factor()

if __name__=="__main__":
    main()