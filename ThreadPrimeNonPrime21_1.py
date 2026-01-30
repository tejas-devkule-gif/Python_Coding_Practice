import threading

def Prime(no):
    for i in range(2,no):
        if no % i ==0:
            return
    print("Prime No")

def NonPrime(no):
    for i in range(2,no):
        if no % i ==0:
            print("Not Prime No")
            return

num=int(input("Enter number :"))

if __name__=="__main__":
    
    s1=threading.Thread(target=Prime, args=(num,))
    s2=threading.Thread(target=NonPrime,args=(num,))

    s1.start()
    s2.start()

    s1.join()
    s2.join()
    
    print("End of main thread")
