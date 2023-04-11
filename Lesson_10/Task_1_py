letter_list = ['разработка', 'сокет', 'декоратор']

def encode_to_unicode_escape(letter_list):
    unicode_list = []
    for i in range(len(letter_list)):
        s = letter_list[i].encode('unicode_escape').decode()
        unicode_list.append(s)
    return unicode_list


def type_verif(result_list):
    for i in range(len(result_list)):
            print(
            '"{}"'.format(result_list[i]),
            "использует тип: ",
            type(result_list[i]))


print(letter_list)
type_verif(letter_list)
unicode_list = encode_to_unicode_escape(letter_list)
print(unicode_list)
type_verif(unicode_list)