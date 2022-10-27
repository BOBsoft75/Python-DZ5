# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


string = str(input('Введите изначальный текст: '))
letter = str(input('Удалить из текста слова содержащие: '))
sub_string = string.lower().replace(',', ' , ').replace('.', ' . ')
words = sub_string.split()
new_words = []
for word in words:
    if letter not in word.lower():
        new_words.append(word)

new_words = ' '.join(new_words)
print()
print(f'Изначальный текст: {string}')
print(f'Текст без слов содержащих "{letter}": {new_words}')
exit()
