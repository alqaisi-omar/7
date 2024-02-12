def print_divisors(n):
    """Выводит все делители числа n через пробел."""
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    print(" ".join(map(str, divisors)))

# Ввод числа
number = int(input("Введите число: "))

# Вывод делителей
print("Делители числа", number, ":", end=" ")
print_divisors(number)
