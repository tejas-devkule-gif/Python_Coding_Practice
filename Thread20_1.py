import threading

def Even():
    for i in range(1,11):
        if i % 2 ==0:
            print("Even :",i)

def Odd():
    for i in range(1,11):
        if i % 2 ==1:
            print("Odd :",i)
    

if __name__=="__main__":
    
    s1=threading.Thread(target=Even)
    s2=threading.Thread(target=Odd)

    s1.start()
    s2.start()

    s1.join()
    s2.join()

    print("End of main thread")