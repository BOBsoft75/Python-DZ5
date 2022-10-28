# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


r = open('text1.txt', 'r', encoding="utf-8")
string2 = r.read()

print(f'Строка из файла: {string2}\n')
my_dict = {}
result_string = ''
for letter in string2:
    if not my_dict.get(letter):
        my_dict[letter] = string2.count(letter)
        result_string += str(string2.count(letter)) + str(letter)
print(f'Сжатая строка: {result_string}')


def rle_mtd(string: str) -> str:
    string_out = ''
    count = 1
    while string:
        if len(string) > 1:
            if string[0] == string[1]:
                count += 1
                string = string[1:]
            else:
                string_out += str(count) + string[0]
                string = string[1:]
                count = 1
        else:
            string_out += str(count) + string[0]
            string = ''

    return string_out


def rle_bck(string: str) -> str:
    string_out = ''
    count = ''
    while string:
        if len(string):
            if string[0].isdigit():
                count += string[0]
                string = string[1:]
            else:
                count = int(count)
                string_out += string[0]*int(count)
                string = string[1:]
                count = ''
        else:
            break
    return string_out


string3 = rle_bck(result_string)
print(f'Разжатая строка: {string3}')
r2 = open('text2.txt', 'w', encoding="utf-8")
r2.write(string3)


exit()


def encode(data_str: str):
    if data_str is None:
        return None
    if (data_len := len(data_str)) == 0:
        return ''
    encoded_str = ''
    series_char = data_str[0]
    count = 1
    i = 1
    while i < data_len:
        char = data_str[i]
        if char != series_char:
            encoded_str += str(count) + series_char
            series_char = char
            count = 1
        else:
            count += 1
        i += 1

    if count > 0:
        encoded_str += str(count) + series_char
    return encoded_str


def decode(data_str: str) -> tuple[str, list]:
    errors_found = []
    if data_str is None:
        return (None, errors_found)
    if (data_len := len(data_str)) == 0:
        return ('', errors_found)
    decoded_str = ''
    i = 0
    qty_str = ''
    while i < data_len:
        item = data_str[i]
        if item.isdigit():
            qty_str += item
        else:
            if qty_str == '':
                errors_found.append(i)
                while i + 1 < data_len and not data_str[i + 1].isdigit():
                    i += 1
            else:
                decoded_str += item * int(qty_str)
                qty_str = ''
        i += 1

    if qty_str != '':
        errors_found.append(data_len - 1)

    return (decoded_str, errors_found)


print(f'Строка из файла: {string2}')
print(f'Сжатая строка: {encode(string2)}')
print()
string3 = encode(string2)
print(f'Сжатая строка: {string3}')
# print(string2)
textEncoded = str(decode(string3))
print(f'Разжатая строка: {textEncoded[2:-6]}')
r2 = open('text2.txt', 'w', encoding="utf-8")
r2.write(string3)

exit()
