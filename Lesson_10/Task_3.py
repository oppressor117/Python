word_list = ['attribute', 'класс', 'функция', 'type']

for word in word_list:
    word_bytes = None
    try:
        word_bytes = bytes(word, 'ascii')
    except:
        print(f"Слово '{word}' невозможно преобразовать в байтовый тип")
        continue
    print(word_bytes)