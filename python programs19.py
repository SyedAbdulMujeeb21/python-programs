a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(str(a) + " is the largest")
elif b >= a and b >= c:
    print(str(b) + " is the largest")
else:
    print(str(c) + " is the largest")