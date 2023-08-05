def get_unique_elements(numbers):
    unique_elements = []
    for num in numbers:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

numbers = [1, 2, 3, 2, 4, 3, 5]
print(get_unique_elements(numbers))  # Выведет [1, 2, 3, 4, 5]







