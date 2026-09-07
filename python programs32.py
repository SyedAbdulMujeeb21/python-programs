n = int(input("Enter a number: "))

if n > 0:
    print(str(n) + " is positive")
    if n % 2 == 0:
        print(str(n) + " is even")
    else:
        print(str(n) + " is odd")
elif n < 0:
    print(str(n) + " is negative")
else:
    print("The number is zero")