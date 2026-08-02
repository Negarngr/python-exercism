def is_armstrong_number(number):
    digits = str(number)
    digit_number = len(digits)
    total = 0
    for i in digits:
        digit = int(i)
        total += digit ** digit_number
    

    return total == number 
   




x=is_armstrong_number(153)

print(x)
