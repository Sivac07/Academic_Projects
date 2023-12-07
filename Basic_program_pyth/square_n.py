def square():
    values = []
    for i in range(1,6):
        a = int(input(f"Enter the {i}th number: "))
        values.append(a)
    print(values)
    for a in values:
        square = a*a
        print(f"The square of the number {a} is " + str(square)) 
square()

