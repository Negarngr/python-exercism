def square(number):

    
        if number > 64 or number < 1 :
            raise ValueError ("square must be between 1 and 64")

        return 2 ** (number-1)
   

def total():
    tot = 0

    for i in range(1,65):
        tot = tot + 2 ** (i-1)

    return tot

