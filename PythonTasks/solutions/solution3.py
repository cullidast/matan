# Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Функция для вычисления суммы четных чисел в заданном диапазоне
def sum_of_even(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0: # Проверяем, является ли число четным
            total_sum += num
    return total_sum

# Получаем начало и конец диапазона от пользователя
start_range = int(input("Введите начало диапазона: "))
end_range = int(input("Введите конец диапазона: "))

# Вызываем функцию для вычисления суммы четных чисел
even_sum = sum_of_even(start_range, end_range)

# Выводим результат
print(f"Сумма четных чисел в заданном диапазоне от {start_range} до {end_range}: {even_sum}")

