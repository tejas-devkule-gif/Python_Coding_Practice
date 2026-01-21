# Write a program which accepts length and width of rectangle and prints area.

def AreaOfRectangle(len,wid):
    return(len*wid)

def main():

    length=0
    width=0
    Ret=False
    
    length= int(input("Enter length of Rectangle :"))
    width=int(input("Enter width of Rectangle :"))

    Ret=AreaOfRectangle(length,width)
    print("Area of Rectangle is :",Ret)

if __name__=="__main__":
    main()