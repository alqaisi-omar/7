import math

def median(a, b, c):
    """Вычисляет медиану треугольника."""
    # Используем формулу медианы
    median_length = 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)
    return median_length
# Ввод длин сторон исходного треугольника
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

# Вычисление медиан треугольника
median_to_a = median(b, c, a)
median_to_b = median(a, c, b)
median_to_c = median(a, b, c)

# Вывод результатов
print("Медиана, проведенная к стороне a:", median_to_a)
print("Медиана, проведенная к стороне b:", median_to_b)
print("Медиана, проведенная к стороне c:", median_to_c)
