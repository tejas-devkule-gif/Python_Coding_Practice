# Write a program which accepts marks and display grade.

def main():

    marks=int(input("Enter the marks of student :"))
    
    if marks>=75:
        print("Distinction")
    elif marks>=60:
        print("First Class")
    elif marks>=50:
        print("Second Class")
    elif marks<50:
        print("Fail")
    else:
        print("Enter valid marks")


if __name__=="__main__":
    main()