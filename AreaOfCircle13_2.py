# Write a program which accepts radius of circle and prints area of circle.

def AreaOfCircle(rad):
    return(22/7*rad**2)   # or (3.14*rad**2)

def main():

    radius=0
    
    Ret=False
    
    radius= int(input("Enter radious of Circle :"))

    Ret=AreaOfCircle(radius)
    print("Area of Circle is :",Ret)

if __name__=="__main__":
    main()