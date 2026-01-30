import threading

def Thread1(lst):
    max=List[0]
    for no in lst:
        if no > max:
            max=no
    print("Maximum No",max)    
    
            
def Thread2(lst):
    min=List[0]
    for no in lst:
        if no < min:
            min=no
    print("Minimum No",min)  
    

List=list(map(int,input("Enter numbers :").split()))    

if __name__=="__main__":
    
    s1=threading.Thread(target=Thread1,args=(List,))
    s2=threading.Thread(target=Thread2,args=(List,))

    s1.start()
    s2.start()
    s1.join()
    s2.join()

    print("End of main thread")