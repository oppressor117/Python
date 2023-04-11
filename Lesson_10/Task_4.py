word_list = ['разработка', 'администрирование', 'protocol', 'standard']
print(word_list)
for word in word_list:
     word_bytes = word.encode('utf-8')
     print(f'В байтовом представлении: {word_bytes.hex()}')
     word_str = bytes.decode(word_bytes, 'utf-8')
     print(f'В строковом представлении: {word_str} \n')