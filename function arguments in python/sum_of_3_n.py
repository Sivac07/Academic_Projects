a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
def input(a,b,c):
    print("Sum of the number is ", str(a+b+c))
def process(a,b,c):
    if a == b == c:
        sum = a+b+c
        return sum*3
    else:
        square = lambda x: x**2
        return square(a), square(b),square(c)
input(a,b,c)
outcome = process(a,b,c)
if outcome:
    print(f"The values are eqaul. The thrice of the number is {outcome}")
else:
    print("Values are not equal. Sqaure of the numbers:")
    for i in process:
        print(i)

