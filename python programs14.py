n = int(input("Enter a number: "))
k = int(input("Enter the bit position (K): "))

if (n >> k) & 1:
    print("Bit " + str(k) + " is set")
else:
    print("Bit " + str(k) + " is not set")