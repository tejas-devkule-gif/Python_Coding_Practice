# Write a program which accepts one character and checks whether it is vowel or consonant.
def VowelChk():
    char=input("Enter any character :")
    vowel=["a","e","i","o","u","A","E","I","O","U"]
    count=False

    for i in vowel:
        if char==i:
            count=True
            break

    if count:
        print("It is vowel")
    else:
        print("It is consonant")

# if char in viwel:
#    print("Vowel")
# else:
#    print("consonant")

def main():
    VowelChk()
if __name__=="__main__":
    main()