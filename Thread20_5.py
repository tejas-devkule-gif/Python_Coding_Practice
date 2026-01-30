import threading

def Thread1():
    for i in range(1,51):
        print(i)
    print("-"*5)
            
def Thread2():
    for i in range(50,0,-1):
        print(i)
    
if __name__=="__main__":
    
    s1=threading.Thread(target=Thread1)
    s2=threading.Thread(target=Thread2)

    s1.start()
    s1.join()
    
    s2.start()
    s2.join()
    
    print("End of main thread")