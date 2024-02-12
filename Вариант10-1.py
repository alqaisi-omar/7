def count_numbers_with_digits(a, b, c, N):
    """Находит количество чисел на отрезке [100, N], составленных из цифр a, b, c."""
    count = 0
    for num in range(100, N + 1):
        digits = set(str(num))
        if str(a) in digits and str(b) in digits and str(c) in digits:
            count += 1
    return count

# Ввод значений a, b, c и N
a = int(input("Введите цифру a: "))
b = int(input("Введите цифру b: "))
c = int(input("Введите цифру c: "))
N = int(input("Введите верхнюю границу интервала N (210 < N < 231): "))

# Поиск количества чисел
count = count_numbers_with_digits(a, b, c, N)
print("Количество чисел на отрезке [100, {}], составленных из цифр {}, {} и {}: {}".format(N, a, b, c, count))
