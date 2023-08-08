def replace_repetive_chars(s):
    # Используем list для создания изменяемой строки
    chrar_list = list(s)

    #Используем set для отслеживания уникальных символов, которые мы уже видели
    seen_chars = set()

    for i, char in enumerate(char_list):
        # Если символ уже видели, заменяем его на '*'
        if char in seen_chars:
            char_list[i] = '*'
        # Иначе добовляем его в набор уникальных символов
        else:
            seen_chars.add(char)

    # Преобразуем list обратно в строку
    return ''.join(char_list)

s = "aabcbc"
print(replace_repetitive_chars(s)) # Выведет "abc*c"
        
