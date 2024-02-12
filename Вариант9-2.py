def array_statistics(arr):
    """Вычисляет произведение элементов и среднее арифметическое значение массива."""
    product = 1
    for num in arr:
        product *= num
    average = sum(arr) / len(arr)
    return product, average

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
    product, average = array_statistics(arr)
    print(f"Для массива {i+1}:")
    print(f"Произведение элементов: {product}")
    print(f"Среднее значение: {average}")
