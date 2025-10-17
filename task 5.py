def palindrome(s):
    # Игнорир регистра и пробелов
    s = ''.join(s.lower().split())
    return s == s[::-1]

def pochti_palindrome(s):
    # приводим строку к нижнему регистру без пробелов
    normalized = ''.join(s.lower().split())
    
    # Проверка на палиндром
    if palindrome(s):
        print("палиндром")
        return "палиндром"
    
    # Проверка на почти палиндром
    left, right = 0, len(normalized) - 1
    
    while left < right:
        if normalized[left] != normalized[right]:
            # Проверяем возможность удаления одного символа
            # Вариант 1: удаляем символ слева
            without_left = normalized[:left] + normalized[left+1:]
            # Вариант 2: удаляем символ справа
            without_right = normalized[:right] + normalized[right+1:]
            
            if without_left == without_left[::-1] or without_right == without_right[::-1]:
                print("почти палиндром")
                return "почти палиндром"
            else:
                print("не палиндром")
                return "не палиндром"
        
        left += 1
        right -= 1
    
    return "палиндром"

pochti_palindrome('фоноф    ')