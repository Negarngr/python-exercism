def is_armstrong_number(number):
    digits = str(number)
    digit_number = len(digits)
    total = sum(int(i) ** digit_number for i in digits)
    return total == number


print(is_armstrong_number(153))