def gcd(a, b):
    """Алгоритм Евклида для нахождения наибольшего общего делителя."""
    while b != 0:
        a, b = b, a % b
    return a

def subtract_fractions(a, b, c, d):
    """Вычитание дробей."""
    # Находим общий знаменатель
    common_denominator = b * d

    # Приводим числители к общему знаменателю
    numerator1 = a * d
    numerator2 = c * b

    # Вычитаем числители
    result_numerator = numerator1 - numerator2

    # Находим наибольший общий делитель для сокращения дроби
    greatest_common_divisor = gcd(result_numerator, common_denominator)

    # Сокращаем дробь
    result_numerator //= greatest_common_divisor
    common_denominator //= greatest_common_divisor

    return result_numerator, common_denominator

# Ввод дробей
a = int(input("Введите числитель первой дроби: "))
b = int(input("Введите знаменатель первой дроби: "))
c = int(input("Введите числитель второй дроби: "))
d = int(input("Введите знаменатель второй дроби: "))

# Вычитание дробей
result_numerator, result_denominator = subtract_fractions(a, b, c, d)
print("Разность дробей:", result_numerator, "/", result_denominator)
