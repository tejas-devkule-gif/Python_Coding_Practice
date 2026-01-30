from functools import reduce
def ChkPrime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def main():
    List=list(map(int,input("Enter numbers :").split()))
    print(List)

    FData=list(filter(ChkPrime,List))
    print(FData)

    MData=list(map(lambda no : no * 2,FData))
    print(MData)

    RData=reduce(lambda x,y: x if(x > y)  else y,MData)
    print("Maximum is :",RData)

if __name__=="__main__":
    main()