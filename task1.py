def reverse_words_forming_blocks():  
    try:
        with open("reverse_and_blocks_task_1.txt", "r", encoding="utf-8") as f:
            sentences = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Файл 'everse_and_blocks_task_1.txt' не найден!")
        return
    
    BLOCK_SIZE = 2
    
    blocks = []
    for i in range(0, len(sentences), BLOCK_SIZE):
        block = sentences[i:i + BLOCK_SIZE]
        blocks.append(block)
    
    result = []
    for block in blocks:
        processed_block = []
        for sentence in block:
            words = sentence.split()  
            reversed_sentence = " ".join(words[::-1])  
            processed_block.append(reversed_sentence)
        result.append(processed_block)

    print("Текст из файла:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
    
    print("\nТекст после работы функции:")
    for i, block in enumerate(result, 1):
        print(f"Блок {i}:")
        for sentence in block:
            print(f"  {sentence}")
        print()
reverse_words_forming_blocks()