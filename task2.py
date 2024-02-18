from collections import deque

def is_palindrome(string):
    # Видаляємо пробіли і переводимо рядок до нижнього регістру
    string = string.replace(" ", "").lower()
    
    # Створюємо двосторонню чергу та додаємо символи рядка
    char_queue = deque()
    for char in string:
        char_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

# Приклад використання
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # Виведе: True