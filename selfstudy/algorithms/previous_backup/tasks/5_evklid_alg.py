def evklid1(x,y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return(x + y)

x = int(input('please enter the first number for evklid1: '))
y = int(input('please enter the second number for evklid1: '))
print(evklid1(x,y))

########################################

def evklid2(x,y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return(x)

x = int(input('please enter the first number for evklid2: '))
y = int(input('please enter the second number for evklid2: '))
print(evklid2(x,y))