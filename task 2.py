def compress_string(s):
    if len(s) <= 2:
        return s
    
    compressed = []
    count = 0
    
    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed.append(s[i])
            if count > 1:
                compressed.append(str(count))
            count = 0
    
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

def test_compression():
    """
    Функция для тестирования различных случаев
    """
    test_cases = [
        "aaabbc",      # → "a3b2c"
        "abcd",        # → "abcd" (сжатая не короче)
        "a",           # → "a"
        "aa",          # → "aa" (a2 длиннее!)
        "aaa",         # → "a3"
        "aabb",        # → "aabb" (a2b2 той же длины)
        "aaab",        # → "aaab" (a3b той же длины)
        "aa    abb",       # → "a3b2"
        "",            # → ""
        " ",           # → " "
        "   ",         # → " 3" (но пробелы тоже сжимаются!)
        "a" * 10,      # → "a10"
        "abc" * 3,     # → "abcabcabc" (не сжимается)
    ]
    
    print("Тестирование сжатия строк:")
    print("=" * 50)
    

    for test in test_cases:
        result = compress_string(test)
        print(f"Вход: '{test}' ({len(test)} симв.) → '{result}' ({len(result)} симв.)")
test_compression()