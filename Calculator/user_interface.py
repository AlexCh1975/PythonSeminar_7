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
    for key in keys: 
        print(f'"{key}"')
        meaning = input()
        if meaning:
            operator[key] = meaning
            if operator: break  
     
    for i in operator:
        if operator[i]: data.insert(0, key) 
        else:
            print("Вы не выбрали операцию!")
            exit()
    print("------------------------------------------------------------")
    return data
    print()

def print_result(res):
    print(f'result = {res}')
