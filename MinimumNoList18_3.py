def MinOfList(list):
    min = list[0]
    for i in list:
        if i<min:
            min=i
    return min

numbers = list(map(int,input("Enter numbers :").split()))
print(MinOfList(numbers))