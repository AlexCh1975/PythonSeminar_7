from datetime import datetime as dt
from time import strftime

def all_logger(result, data):
    operation = data[0]
    a = data[1]
    b = data[2]
    if operation == 'mult': operation = '*' 
    elif operation == 'div': operation = '/' 
    elif operation == 'int_div': operation = '//' 
    elif operation == 'rem_of_div': operation = '%' 
    elif operation == 'pow': operation = '^' 
    elif operation == 'sgrt': operation = 'sgrt' 
    elif operation == 'sum': operation = '+' 
    elif operation == 'sub': operation = '-' 
    else: operation = ('Operation is not possible!')

    time = dt.now().strftime('%H:%M')
    with open('log_calc.csv', 'a', encoding='utf-8') as file:
        file.write('{};{}{}{}={}\n'.format(time, a, operation, b, result))