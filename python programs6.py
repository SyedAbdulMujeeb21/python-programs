a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(str(a) + " is greater")
elif b > a:
    print(str(b) + " is greater")
else:
    print("Both numbers are equal")