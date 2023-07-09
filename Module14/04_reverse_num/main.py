def reverse_float(num):
    digits = str(num).split('.')
    reversed_digits = [''.join(reversed(part)) for part in digits]

    return float( '.'.join(reversed_digits) )

a = reverse_float(input("Введите первое число: "))
b = reverse_float(input("Введите второе число: "))

print('Первое число наоборот: ', a)
print('Второе число наоборот: ', b)
print('Сумма: ', a + b)


