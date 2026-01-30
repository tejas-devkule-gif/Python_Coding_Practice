import threading

def EvenList(brr):
    even=[]
    sum=0
    for i in brr:
        if i % 2 ==0:
            even.append(i)
            sum=sum+i
  
    print("even list :",even)
    print("Sum of even list :",sum)
            

def OddList(crr):
    odd=[]
    sum=0
    for i in crr:
        if i % 2 ==1:
            odd.append(i)
            sum=sum+i
    
    print("odd list :",odd)
    print("Sum of odd list :",sum)

List=list(map(int,input("Enter numbers :").split()))    

if __name__=="__main__":
    
    s1=threading.Thread(target=EvenList,args=(List,))
    s2=threading.Thread(target=OddList,args=(List,))

    s1.start()
    s2.start()

    s1.join()
    s2.join()

    print("End of main thread")