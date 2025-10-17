def brackets_check(text):
    stack = []
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    opening_brackets = set(bracket_pairs.values())
    closing_brackets = set(bracket_pairs.keys())
    
    for char in text:
        if char in opening_brackets:
            # видим открывающую скобку (,[,{ - добавляем в stack
            stack.append(char)
        elif char in closing_brackets:
            # Если встречаем закрывающую скобку
            if not stack:
                # stack пустой - нет открывающей скобки
                return False
            
            #соответствует ли последняя открывающая скобка текущей закрывающей
            last_opening = stack.pop()
            if last_opening != bracket_pairs[char]:
                return False
    
    # Если stack пуст - все скобки правильно закрыты
    return len(stack) == 0