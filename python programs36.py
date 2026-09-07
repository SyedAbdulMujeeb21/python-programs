cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    print("Profit = " + str(profit))
elif cp > sp:
    loss = cp - sp
    print("Loss = " + str(loss))
else:
    print("No profit, no loss")