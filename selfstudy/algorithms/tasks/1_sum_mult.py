# x=abs(int(input('введите целое число: ')))

# summ = 0

# if x == 0:
#     mult = 0
# else:
#     mult = 1

# while x > 0:
#     digit = x%10
#     summ += digit
#     mult *= digit
#     x = x//10

# print('Сумма: ', summ)
# print('Произведение: ', mult)

##############################

x = input('Please enter the number: ')

summ = 0
if x == '0':
    mult = 0
else:
    mult = 1

for n in x:
    summ += int(n)
    mult *= int(n)

print('summ = ', summ)
print('mult = ', mult)