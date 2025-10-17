import random
import re
import os

def erase_text_simple(input_file, erase_percent):
    # Читаем файл
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Случайно выбираем метод
    method = random.choice(['words', 'sentences'])
    
    if method == 'words':
        # Стираем случайные слова
        words = re.findall(r'\b\w+\b', text)
        to_remove = set(random.sample(words, max(1, int(len(words) * erase_percent / 100))))
        result = re.sub(r'\b\w+\b', lambda m: '...' if m.group() in to_remove else m.group(), text)
    else:
        # Стираем части предложений
        sentences = re.split(r'([.!?]+)', text)
        for i in range(0, len(sentences), 2):
            if i < len(sentences) and random.random() < erase_percent / 100:
                words = sentences[i].split()
                if len(words) > 3:
                    remove_count = min(2, len(words) - 2)
                    start = random.randint(1, len(words) - remove_count - 1)
                    sentences[i] = ' '.join(words[:start]) + ' ... ' + ' '.join(words[start + remove_count:])
        result = ''.join(sentences)
    
    # Сохраняем результат
    output_file = f"{os.path.splitext(input_file)[0]}_erased.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"Готово! Файл сохранен как: {output_file}")
    print(f"Использован метод: {'стирание слов' if method == 'words' else 'стирание частей предложений'}")
    return output_file



filename = input("Введите имя файла: ")
percent = float(input("Введите процент удаления: "))
erase_text_simple(filename, percent)