import re

country_code = '1'
file_name = "pr4_test.txt"
pattern = r'\+\d{11}'
# общий паттерн для поиска номеров телефона
# не искпользовал ([\s\n\-\(\)]*\d){10}, а просто скопировал 10 раз, тк со скобками не работает поиск корректно
#pattern = r'\+?[\s\n\-\(\)]*\d?[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d[\s\n\-\(\)]*\d'


def get_digits(text):
    num = ''
    for n in text:
        if n.isdigit():
            num+=n
    return num


with open(file_name, mode="r", encoding="utf-8") as file:
    text = file.read()
    res = re.findall(pattern, text)
    print('Res', res)
    for number in res:
        #в каждом найденном номере, ищем только цифры и переводим их в нужный формат
        number = ''.join(number)
        num = get_digits(number)
        # тк тф может быть без кода страны - вначале проверяем кол-во цифр в номере (10, если без кода страны)
        new_num = '+'+ country_code
        if len(num) == 10:
            new_num = new_num + '('+num[0:3]+')'+num[3:6]+'-'+num[6:8]+'-'+num[8:]
        else:
            new_num = new_num + '('+num[1:4]+')'+num[4:7]+'-'+num[7:9]+'-'+num[9:]
        text = text.replace(number, new_num)

    # save to file
    new_file = open('res_'+file_name, mode="w", encoding="utf-8")
    new_file.write(text)
    new_file.close()
