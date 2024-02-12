def array_statistics(arr):
    """Вычисляет сумму элементов и среднеарифметическое значение массива."""
    sum_elements = sum(arr)
    average = sum_elements / len(arr)
    return sum_elements, average

# Ввод трех массивов и вычисление их статистики
arrays = []
for i in range(3):
    arr = []
    n = int(input(f"Введите количество элементов для массива {i+1}: "))
    for j in range(n):
        arr.append(int(input(f"Введите элемент {j+1}: ")))
    arrays.append(arr)

# Вывод статистики для каждого массива
for i, arr in enumerate(arrays):
    sum_elements, average = array_statistics(arr)
    print(f"Для массива {i+1}:")
    print(f"Сумма элементов: {sum_elements}")
    print(f"Среднее значение: {average}")
