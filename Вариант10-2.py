def reverse_words(sentence):
    """Изменяет последовательность слов в строке на обратную."""
    words = sentence.split()  # Разбиваем строку на слова
    reversed_sentence = " ".join(reversed(words))  # Обратно соединяем слова в строку
    return reversed_sentence

# Ввод строки
sentence = input("Введите строку: ")

# Получение результата
reversed_sentence = reverse_words(sentence)
print("Результат:", reversed_sentence)
