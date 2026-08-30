def square_of_sum(number):

    total = 0
    for i in range(1 , number+1):
        total += i
    return total**2

def sum_of_squares(number):

    total_sq = 0
    for i in range (1 , number+1):
        total_sq += i**2
    return total_sq

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)  
