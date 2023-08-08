Задача: Замена повторяющихся символов
Напишите функцию на Python, которая принимает строку и возвращает новую строку с замененными повторяющимися символами. Заменяет она следующим образом: первое вхождение символа остается без изменений, все последующие вхождения символа заменяются на символ ''. Например, для строки "aabcbc" функция должна вернуть "abcc".Задача: Замена повторяющихся символов
Напишите функцию на Python, которая принимает строку и возвращает новую строку с замененными повторяющимися символами. Заменяет она следующим образом: первое вхождение символа остается без изменений, все последующие вхождения символа заменяются на символ ''. Например, для строки "aabcbc" функция должна вернуть "abcc".


Примеры

replace_repetitive_chars("aabcbc")  # Возвращает "abc*c"
replace_repetitive_chars("hello")   # Возвращает "h*elo"
replace_repetitive_chars("mississippi")  # Возвращает "m*is*ipi"

Описание решения
Для решения данной задачи используется функция replace_repetitive_chars, которая проходит по строке и заменяет все повторяющиеся символы, кроме первого вхождения, на символ '*'. Для этого функция использует список (list) для создания изменяемой строки и множество (set) для отслеживания уникальных символов. Затем функция объединяет элементы списка обратно в строку с помощью метода join.