"""
Sum of Squares
Given a positive integer up to 1,000,
return the sum of all the integers squared from 1 up to the number."""

def sum_of_squares(n):
    
    total = 0

    for number in range(1, n +1):
        total += pow(number, 2)
        
    print(f"{total}")
   
    return total

sum_of_squares(5) #  55.
sum_of_squares(10) #  385.
sum_of_squares(25) #  5525.
sum_of_squares(500) #  41791750.
sum_of_squares(1000) #  333833500.