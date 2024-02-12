def sum_of_digits(n):
    """Вычисляет сумму цифр числа."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def steps_to_zero(n):
    """Определяет количество шагов для получения нуля."""
    steps = 0
    while n > 0:
        n -= sum_of_digits(n)
        steps += 1
    return steps

# Ввод числа
number = int(input("Введите число: "))

# Определение количества шагов
steps = steps_to_zero(number)
print("Для достижения нуля потребуется", steps, "шаг(а/ов).")
