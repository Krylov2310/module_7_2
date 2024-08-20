print('\033[30m\033[47mДомашнее задание по теме "Позиционирование в файле"."\033[0m')
print('\033[30m\033[47mЗадача "Записать и запомнить":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, j in enumerate(strings):
        i = i+1
        cursor = (i, file.tell())
        strings_positions[cursor] = j
        file.write(f'{j}\n')
    file.close()
    return strings_positions


# Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
print()
print(thanks)
