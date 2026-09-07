a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = (b * b) - (4 * a * c)

if discriminant > 0:
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    print("Roots are real and different")
    print("Root 1 = " + str(root1))
    print("Root 2 = " + str(root2))
elif discriminant == 0:
    root1 = -b / (2 * a)
    print("Roots are real and equal")
    print("Root = " + str(root1))
else:
    real_part = -b / (2 * a)
    imaginary_part = (-discriminant) ** 0.5 / (2 * a)
    print("Roots are imaginary")
    print("Root 1 = " + str(real_part) + " + " + str(imaginary_part) + "i")
    print("Root 2 = " + str(real_part) + " - " + str(imaginary_part) + "i")