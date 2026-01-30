import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter
    for i in range(5):       
        lock.acquire()
        counter += 1
        lock.release()

if __name__ == "__main__":

    s1 = threading.Thread(target=Increment)
    s2 = threading.Thread(target=Increment)
    s3 = threading.Thread(target=Increment)

    s1.start()
    s2.start()
    s3.start()

    s1.join()
    s2.join()
    s3.join()

    print("Final value of counter:", counter)