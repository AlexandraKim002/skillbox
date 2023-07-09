print("Введите первую точку")
x01 = float(input('X: '))
y01 = float(input('Y: '))

print("\nВведите вторую точку")
x02 = float(input('X: '))
y02 = float(input('Y: '))

x_difference = x01 - x02
y_difference = y01 - y02

if x_difference == 0:
    k = 1

else:
    k = y_difference / x_difference
b = y02 - k * x02

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)