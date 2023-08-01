print("Введите первую точку")
x01 = float(input('X: '))
y01 = float(input('Y: '))

print("\nВведите вторую точку")
x02 = float(input('X: '))
y02 = float(input('Y: '))

x_difference = x02 - x01
y_difference = y02 - y01

if x_difference != 0:
    k = y_difference / x_difference
    b = y02 - k * x02
    print("Уравнение прямой, проходящей через эти точки:")
    print("y =", k, "* x +", b)
else:
    print("Уравнение вертикальной линии, проходящей через эти точки:")
    print("x =", x01)



