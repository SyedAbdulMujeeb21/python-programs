a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    smallest = a
    if b <= c:
        middle = b
        largest = c
    else:
        middle = c
        largest = b
elif b <= a and b <= c:
    smallest = b
    if a <= c:
        middle = a
        largest = c
    else:
        middle = c
        largest = a
else:
    smallest = c
    if a <= b:
        middle = a
        largest = b
    else:
        middle = b
        largest = a

print("Ascending order: " + str(smallest) + ", " + str(middle) + ", " + str(largest))