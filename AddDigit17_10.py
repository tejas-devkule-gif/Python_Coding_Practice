def CountDigits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10 #removes last digit
    return total

num = int(input("Enter a number: "))
print(CountDigits(num))