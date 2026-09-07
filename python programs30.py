a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b == 0:
        result = "Error: Division by zero"
    else:
        result = a / b
else:
    result = "Invalid operator"

print("Result:", result)