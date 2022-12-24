
# def creating():
#     file = open ('DB.csv', 'w')
#     # with open (file, 'a') as data_csv:
#     file.write('id | first_name | last_name | phone_num | comment\n')
# creating()

def give_int(input_number) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = int(input(input_number))  
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')


def add_row():
    """Принимает имя файла
    Реализует добавление строки и заполнение её полей вводом значений через консоль позльзователем
    Ничего не возвращает, может пинговать об успешном добавлениив консоль"""

    input_data = []
    id = give_int('Введите порядковый номер: ')
    input_data.append(id)
    first_name = input('Введите имя: ')
    input_data.append(first_name)
    last_name = input('Введите Фамилию: ')
    input_data.append(last_name)   
    phone_num = give_int('Введите телефон: ')        
    input_data.append(phone_num)
    comment = input('Введите комментарий: ')
    input_data.append(comment)
    file = open ('DB.csv', 'a')
    file.write(f'{input_data[0]}|{input_data[1]}|{input_data[2]}|{input_data[3]}|{input_data[4]}\n')

add_row()
