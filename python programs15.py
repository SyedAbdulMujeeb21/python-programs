n = int(input("Enter a number: "))

count = 0
temp = n

while temp > 0:
    count = count + (temp & 1)
    temp = temp >> 1

print("Number of set bits in " + str(n) + " is " + str(count))