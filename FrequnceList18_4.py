def Frequency(list, num):
    count = 0
    for i in list:
        if i == num:
            count += 1
    return count


def main():
    n = int(input("Enter number of elements: "))
    list = []

    for i in range(n):
        value = int(input("Enter element: "))
        list.append(value)
    num = int(input("Enter number to find frequency: "))

    result = Frequency(list, num)
    print("Frequency of", num, "is:", result)


if __name__ == "__main__":
    main()
