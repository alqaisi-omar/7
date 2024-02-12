import math

def square_triangle(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона."""
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def square_rectangle(a, b):
    """Вычисляет площадь прямоугольника."""
    return a * b

def square_circle(r):
    """Вычисляет площадь круга."""
    return math.pi * r ** 2

# Запрос у пользователя выбора фигуры и ввод параметров
print("Выберите фигуру для вычисления площади:")
print("1. Треугольник")
print("2. Прямоугольник")
print("3. Круг")

choice = int(input("Введите номер: "))

if choice == 1:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    result = square_triangle(a, b, c)
    print("Площадь треугольника:", result)
elif choice == 2:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    result = square_rectangle(a, b)
    print("Площадь прямоугольника:", result)
elif choice == 3:
    r = float(input("Введите радиус круга: "))
    result = square_circle(r)
    print("Площадь круга:", result)
else:
    print("Ошибка: такой фигуры не существует.")
