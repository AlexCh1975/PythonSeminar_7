import logger as log

def ui_interaction():

    print("Выберите тип числа ('' (нет), 1 (да)):")
    rational_num = input("Рациональное: ")
    complex_num = input("Комплексное: ")

    if not rational_num and not complex_num:
        print("Вы не выбрали тип числа!")
        exit()
    print("------------------------------------------------------------")
    data = []
    if rational_num and not complex_num:
        for i in range(2):
            data.append(input("Введите число: "))
    elif not rational_num and complex_num:
        for i in range(2):
            data.append(input("Введите комплексное число 2+4j': "))
    elif rational_num and complex_num:
        for i in range(2):
            data.append(input("Введите число (или комплексное число 2-4j): "))
    else:
        print("Не выбрано не одного числа!")
        exit()
    print("------------------------------------------------------------")

    print("Выберите тип операции('' (нет), 1(да)):")
     
    operator = {}
    keys = ['mult', 'div', 'int_div', 'rem_of_div', 'pow', 'sqrt', 'sum', 'sub']
    keys_sing = [' * ', ' / ', ' // ', ' % ', ' ^ ', ' sqrt ', ' + ', ' - ']
    k = 0
    data = list(filter(lambda x: x != "", data))
    if len(data) == 1:
        print(f"{'sqrt'}")
        meaning = input()
        if meaning:
            operator['sqrt'] = meaning
    else:
        for key in keys: 
            print(f"{keys_sing[k]}")
            meaning = input()
            k += 1
            if meaning:
                operator[key] = meaning
                if operator: break  
        
    for key in operator:
        if operator[key]: data.insert(0, key) 
        else:
            print("Вы не выбрали операцию!")
            exit()
    print("------------------------------------------------------------")
    return data
    print()

def print_result(res, data):
    print(data)
    keys = {'mult': '*', 'div': '/', 'int_div': '//', 'rem_of_div': '%', 'pow': '^', \
        'sqrt': 'sqrt', 'sum': '+', 'sub': '-'}
    op = ''
    if len(data) == 3:
        for key in keys:
            if data[0] == key: op = keys[key]
        print(f'{data[1]} {op} {data[2]} = {res}')
    else:
        for key in keys:
            if data[0] == key: op = keys[key]
        print(f'{data[1]} {op} = {res}')
