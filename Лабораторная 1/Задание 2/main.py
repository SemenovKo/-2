from task_1 import Pelmeni, Flask, Printer

if __name__ == "__main__":
    printer_1 = Printer('средний', True)
    flask_1 = Flask('неон', 5, 1)
    pelmeni_1 = Pelmeni(5, 'говядина')

    try:
        print(printer_1.add_paper(1.1))
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        flask_1.change_temp('10')
        print(flask_1.change_temp('10'))
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        pelmeni_1.check_price('two')
    except TypeError:
        print('Ошибка: неправильные данные')
