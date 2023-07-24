import math

def minimal_delit(number):
    if number < 2:
        return None

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return i

    return number

number = int(input("Введите число: "))
result = minimal_delit(number)
if result:
    print("Наименьший делитель, отличный от единицы:", result)
else:
    print("Число должно быть больше или равно 2.")
