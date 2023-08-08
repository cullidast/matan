def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start_range = int(input("Введите начало диапазона: "))
end_range = int(input("Введите конец диапазона: "))

prime_numbers = find_primes_in_range(start_range, end_range)
print("Простые числа в заданном диапазоне:", prime_numbers)




