def check_number_range(number):
    if number < 100:
        return False, "Number is less than 100"
    elif 100 <= number < 1000:
        return True, "Number is within 100 to 999"
    elif 1000 <= number <2000:
        return True, "Number is within 1000 to 1999"
    elif number >= 2000:
        return False, "Number is 2000 or greater"
input_number = int(input("Enter a number: "))
is_within_range, range_message = check_number_range(input_number)
print(is_within_range)
print(range_message)

    
    
    
