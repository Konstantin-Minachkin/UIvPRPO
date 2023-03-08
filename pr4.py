import re

file_name = "pr4_test.txt"
pattern = r'\+\d{11}'

with open(file_name, mode="r", encoding="utf-8") as file:
    text = file.read()
    res = re.findall(pattern, text)
    for num in res:
        new_num = '1('+num[2:5]+')'+num[5:8]+'-'+num[8:10]+'-'+num[10:]
        # print('new_num', new_num)
        text = text.replace(num, new_num)
    # print(text)
    # save to file
    new_file = open('res_'+file_name, mode="w", encoding="utf-8")
    new_file.write(text)
    new_file.close()