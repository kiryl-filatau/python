def fibonachi1(x):
    val1 = val2 = 1
    n = 0
    while n < x-2:
        val_sum = val1 + val2
        val1 = val2
        val2 = val_sum
        n += 1
    return(val_sum)

x = int(input('please enter a number fib1: '))
if x <= 2:
    print('please restart the programm and enter value > 2')
    quit()
else:
    print(fibonachi1(x))

########################################

def fibonachi2(x):
    val1 = val2 = 1
    while x > 0:
        val1,val2 = val2,val1 + val2
        x -= 1
    return(val2)

x = int(input('please enter a number fib2: ')) - 2
if x <= 0:
    print('please restart the programm and enter value > 2')
    quit()
else:
    print(fibonachi2(x))

########################################

def fibonachi3(x):
    val1 = val2 = 1
    print(val1, end=' ')
    print(val2, end=' ')
    for i in range(2,x):
        val1,val2 = val2,val1 + val2
        print(val2, end=' ')

x = int(input('please enter a number fib3: '))
if x <= 2:
    print('please restart the programm and enter value > 2')
    quit()
else:
    fibonachi3(x)
    print(end='\n')

########################################

def fibonachi4(x):
    if x in (1,2):
        return 1
    return fibonachi4(x - 1) + fibonachi4(x -2)

x = int(input('please enter a number fib4: '))
if x <= 2:
    print('please restart the programm and enter value > 2')
    quit()
else:
    print(fibonachi4(x))