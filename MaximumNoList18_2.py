def MaxOfList(list):
    max = list[0]
    for i in list:
        if i>max:
            max=i
    return max

numbers = list(map(int,input("Enter numbers :").split()))
print(MaxOfList(numbers))