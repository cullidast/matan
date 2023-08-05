def is_palindrome(s):
    return s == s[::-1]

s = "radar"
print(is_palindrome(s))  # Выведет True
