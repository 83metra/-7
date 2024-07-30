def custom_write(file_name, items):
    str_count = 0                                # счётчик записанных строк
    strings_positions = {}                       # словарь {(<номер строки>, <байт начала строки>) : записываемая строка}
    file = open(str(file_name), 'r+', encoding= 'utf-8')
    for string in items:
        str_count += 1
        strings_positions.update({(str_count, file.tell()): string})
        file.write(f'{string}\n')
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
