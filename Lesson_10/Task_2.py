list_byte = [b'class', b'function', b'method']

for line in list_byte:
    print(f'Тип: {type(line)}')
    print(f'Содержание: {line}')
    print(f'Длина: {len(line)}байт(ов)\n')