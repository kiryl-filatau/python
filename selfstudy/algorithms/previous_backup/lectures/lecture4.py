def is_simple_number(x):
    """if the nuber is simple, 
       x = целое число
       if simple, returns True, else - False
    """
    divisor = 2
    while divisor < x: 
        if x%divisor == 0:
            return False
        divisor += 1
    return True

x = int(input('please enter a number: '))
print (is_simple_number(x))

#===========================================

def factorize_number(x):
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1
    else:
        return('thats it')

x = int(input('please enter a number: '))
print (factorize_number(x))