def sum_even():
    sum_of_evens = 0
    for num in range(100,201):
        if num%2 == 0:
            sum_of_evens += num
    print("Sum of even numbers between 100 and 200: ", sum_of_evens)
sum_even()
