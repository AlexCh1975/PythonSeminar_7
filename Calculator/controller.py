import model_div as div
import model_mult as mult
import model_sub as sub
import model_sum as sum
import model_sqrt as sqrt
import user_interface as ui
import logger as log
import compl 

def button_click():
    data = ui.ui_interaction()
    value = 0
    n_data = [data[0]]
    for i in range(1, len(data)):
        if '+' in data[i] or '-' in data[i] and 'j' in data[i]:
            compl.init(data[i])
            value = compl.get_comples_nums() 
        elif data[i].isdigit() or '.' in data[i]:
            value = float(data[i])
        else:
            print("Некоректный ввод числа!")

        n_data.append(value)
    
    # operation = __import__('model_' + n_data[0])
    # f = globals()[data[0]]
    # f = getattr(operation, data[0])
    # print(f)
    # mult = data[0]
    # operation.init(n_data[1], n_data[2])
    # result = operation.f()
    # log.all_logger(result, n_data)
    # ui.print_result(result)

    if n_data[0] == 'mult':
        mult.init(n_data[1], n_data[2])
        result = mult.mult()
        log.all_logger(result, n_data)
        ui.print_result(result, n_data)
    elif n_data[0] == 'div':
        div.init(n_data[1], n_data[2])
        result = div.div()
        log.all_logger(result, n_data)
        ui.print_result(result, n_data)
    elif n_data[0] == 'sum':
        sum.init(n_data[1], n_data[2])
        result = sum.sum()
        log.all_logger(result, n_data)
        ui.print_result(result, n_data)
    elif n_data[0] == 'sub':
        sub.init(n_data[1], n_data[2])
        result = sub.sub()
        log.all_logger(result, n_data)
        ui.print_result(result, n_data)
    elif n_data[0] == 'pow':
        mult.init(n_data[1], n_data[2])
        result = mult.expo()
        log.all_logger(result, n_data)
        ui.print_result(result, n_data)
    elif n_data[0] == 'rem_of_div':
        div.init(n_data[1], n_data[2])
        result = div.rem_of_div()
        log.all_logger(result, n_data)
        ui.print_result(result, n_data)
    elif n_data[0] == 'int_div':
        div.init(n_data[1], n_data[2])
        result = div.int_div()
        log.all_logger(result, n_data)
        ui.print_result(result, n_data)
    elif n_data[0] == 'sqrt':
        sqrt.init(n_data[1])
        result = sqrt.sqrt()
        log.all_logger(result, n_data)
        ui.print_result(result, n_data)
    



