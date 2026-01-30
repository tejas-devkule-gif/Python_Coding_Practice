from functools import reduce

def main():
    List=list(map(int,input("Enter numbers :").split()))
    print(List)

    FData=list(filter(lambda no : no % 2==0,List))
    print(FData)

    MData=list(map(lambda no : no**2,FData))
    print(MData)

    RData=reduce(lambda x,y: x+y,MData)
    print(RData)

if __name__=="__main__":
    main()