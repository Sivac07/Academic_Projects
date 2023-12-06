def sti():
    str = input("Enter the String: ")
    print("Type after conversion of string to integer", type(str))
    str_to_int = int(str)
    print("Type after conversion of string to integer", type(str_to_int))
def its():
    number = int(input("Enter the number :"))
    print("Type after conversion of string to integer", type(number))
    int_to_str = "{}".format(number)
    print("Type after conversion of string to integer", type(int_to_str))
def main():
    print("1. Convert String to Integer")
    print("2. Convert Integer to String")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sti()
    elif choice == 2:
        its()
    else:
        print("Invalid number")
main()
