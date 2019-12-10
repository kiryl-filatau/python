#to invert any number to oct number viso verso

base = 8
x=int(input())
while x > 0:
    digit=x%base
    print(digit, end='-')
    x//=base
