def is_armstrong_number(number):
    number = str(number)
    digit_number = len(number)
    total = 0
    for i in range(digit_number):
        digit = int(number[i])
        total = total + digit ** digit_number
    number = int(number)

    if total == number :
        return True
    else:
        return False





x=is_armstrong_number(153)

print(x)


