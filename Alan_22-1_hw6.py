import re
with open('mock.txt', 'r', encoding='utf_8') as file :
    mock = file.read()
while True:
    a = input('1 - считать имена, 2 - считать емаил, 3 - считать названия файлов, 4 - считать цвета, 5 - выход')
    try:
        a = int(a)
        if a == 5:
            break
        elif a == 1:
            with open('names.txt', 'w', encoding='utf_8') as file1:
                b = re.findall\
                    (r"(?:[A-Z][a-z\-]+\s[A-Z][A-Za-z']+|[A-Z][a-z\-]+\s[A-Z][a-z]+\s[A-Z][A-Za-z']+)", mock)
                for i in b:
                    file1.write(f'{i}\n')
        elif a == 2:
            with open('emales.txt', 'w', encoding='utf_8') as file2:
                b = re.findall(r'(?:[A-Za-z0-9]+@[0-9a-z]+.[a-z]+|[A-Za-z0-9]+@[0-9a-z]+-[a-z]+.[a-z]+|[A-Za-z0-9]+'
                               r'@[a-z0-9]+.[a-z]+.[a-z]+)', mock)
                for i in b:
                    file2.write(f'{i}\n')
        elif a == 3:
            with open('files.txt', 'w', encoding='utf_8') as file3:
                b = re.findall(r'(?:[A-Z][A-Za-z0-9]+\.[a-z0-9]+|[A-Z]\.[a-z0-9]+)', mock)
                for i in b:
                    file3.write(f'{i}\n')
        elif a == 4:
            with open('colour.txt', 'w', encoding='utf_8') as file4:
                b = re.findall(r'#[A-Za-z0-9]+', mock)
                for i in b:
                    file4.write(f'{i}\n')








    except:
        print('выберите целое число')