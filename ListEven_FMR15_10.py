# write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

def main():
    List=list(map(int,input("Enter list of numbers :").split()))
    print(List)

    FData=len(list(filter(lambda No:No%2==0,List)))
    print("List of Odd numbers is :",FData)


if __name__=="__main__":
    main()