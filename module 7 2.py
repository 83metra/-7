def custom_write(file_name, items):
    anfang = 0 # позиция курсора перед записью
    str_count = 0 # счётчик записанных строк
    strings_positions = {} # словарь {(<номер строки>, <байт начала строки>) : записываемая строка}
    file = open(str(file_name), 'r+', encoding= 'utf-8')
    for string in items:
        anfang = file.tell() # позиция курсора до записи
        file.write(f'{string}\n')
        str_count += 1
        strings_positions.update({(str_count, anfang): string})
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
