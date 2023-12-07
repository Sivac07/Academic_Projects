def greater():
    values = []
    for i in range(1,6):
        a = int(input(f"Enter the {i}th number: "))
        values.append(a)
    print(values)
    count = 0
    for a in values:
        if a > 10:
           count += 1
    print("No. of values which is greater than 10 is " + str(count))
greater()
