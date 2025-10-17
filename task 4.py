import random
import string

def quick_password(length=12):
    if length < 4:
        print("Пароль не может быть меньше 4 символов")
        return None
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = "!@#$%^&*"
    
    all_chars = lower + upper + numbers + symbols

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(numbers),
        random.choice(symbols)
    ]
    
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    random.shuffle(password)
    print(''.join(password))


quick_password(12)
