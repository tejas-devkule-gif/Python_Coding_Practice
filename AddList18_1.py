def SumOfList(list):
    total = 0
    for i in list:
        total = total + i
    return total

numbers = list(map(int,input("Enter numbers :").split()))
print(SumOfList(numbers))