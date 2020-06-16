def to_binary1(x):
    string = ''
    while x > 0:
        string = str(x%2) + string
        x //= 2
    return(string)

x = int(input('please enter a number for to_binary1: '))
print(to_binary1(x))
