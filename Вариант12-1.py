def sum_of_divisors(n):
    """Вычисляет сумму всех делителей числа n (кроме самого числа)."""
    divisors_sum = 1  # Начальное значение суммы делителей
    for i in range(2, int(n ** 0.5) + 1):  # Перебираем делители от 2 до корня из n
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Если делитель не равен корню из n, то добавляем и его "пару"
                divisors_sum += n // i
    return divisors_sum

def find_friendly_numbers(N):
    """Находит все пары дружественных чисел, не превышающих N."""
    friendly_pairs = []
    for a in range(2, N + 1):
        b = sum_of_divisors(a)  # Проверяем, является ли b дружественным числом для a
        if b > a and sum_of_divisors(b) == a:
            friendly_pairs.append((a, b))
    return friendly_pairs

# Ввод числа N
N = int(input("Введите число N: "))

# Поиск дружественных чисел
friendly_pairs = find_friendly_numbers(N)

# Вывод результатов
if friendly_pairs:
    print("Дружественные числа, не превышающие", N, ":")
    for pair in friendly_pairs:
        print(pair)
else:
    print("Дружественные числа, не превышающие", N, "не найдены.")
