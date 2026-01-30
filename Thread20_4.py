import threading

def Small(string):
    count = 0
    for char in string:
        if char.islower():
            count += 1
    print("Number of lowercase characters:", count)
    print("Thread name:", threading.current_thread().name)
    print("Thread id:", threading.get_ident())
    print()

def Capital(string):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    print("Number of uppercase characters:", count)
    print("Thread name:", threading.current_thread().name)
    print("Thread id:", threading.get_ident())
    print()

def Digits(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    print("Number of digits:", count)
    print("Thread name:", threading.current_thread().name)
    print("Thread id:", threading.get_ident())
    print()

Str1 = input("Enter string: ")

if __name__ == "__main__":

    s1 = threading.Thread(target=Small, args=(Str1,))
    s2 = threading.Thread(target=Capital, args=(Str1,))
    s3 = threading.Thread(target=Digits, args=(Str1,))

    s1.start()
    s2.start()
    s3.start()

    s1.join()
    s2.join()
    s3.join()

    print("End of main thread")