def is_armstrong_number(number):
    digits = str(number)
    digit_number = len(digits)
    return number == sum(int(i) ** digit_number for i in digits)


