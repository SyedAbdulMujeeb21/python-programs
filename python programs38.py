num = int(input("Enter a 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

total = (a ** 3) + (b ** 3) + (c ** 3)

if total == num:
    print(str(num) + " is an Armstrong number")
else:
    print(str(num) + " is not an Armstrong number")