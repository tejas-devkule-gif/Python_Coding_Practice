import threading

def EvenFactor(no):
    sum=0
    for i in range(1,no+1):
        if no % i ==0 and i % 2 ==0:
            sum=sum + i
    print("Sum of even factor :",sum)
            

def OddFactor(no):
    sum=0
    for i in range(1,no+1):
        if no % i ==0 and i % 2 ==1:
            sum=sum + i
    print("Sum of odd factor :",sum)

num=int(input("enter number :"))    

if __name__=="__main__":
    iCnt=0
    
    s1=threading.Thread(target=EvenFactor,args=(num,))
    s2=threading.Thread(target=OddFactor,args=(num,))

    s1.start()
    s2.start()
    
    s1.join()
    s2.join()

    print("End of main thread")