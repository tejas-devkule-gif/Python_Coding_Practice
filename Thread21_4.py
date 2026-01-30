import threading

def Thread1(list):
    total=0
    for no in list:
        total=total + no 
    print("Sum of elements :",total)    
    
            
def Thread2(list):
    prod=1
    for no in list:
        prod=prod * no
    print("Product of elements :",prod)  
    

List=list(map(int,input("Enter numbers :").split()))    

if __name__=="__main__":
    
    s1=threading.Thread(target=Thread1,args=(List,))
    s2=threading.Thread(target=Thread2,args=(List,))

    s1.start()
    s2.start()
    s1.join()
    s2.join()

    print("End of main thread")