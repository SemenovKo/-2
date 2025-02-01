# TODO: Подробно описать три произвольных класса

if __name__ == "__main__":
    import doctest

    doctest.testmod()


# TODO: описать класс
class Printer:
    def __init__(self, size: str, has_color: bool):
        """
        Инициализация принтера

        :param size: Размер принтера (например, 'портативный', 'средний', 'большой')
        :param has_color: Принтер цветной или черно-белый (True, False)

        Пример:
        >>> printer = Printer('большой', True)
        """

        if size not in {'портативный', 'средний', 'большой'}:
            raise ValueError("Размер должен быть: 'портативный', 'средний', 'большой'")
        self.size = size
        self.has_color = has_color

    def describe(self) -> str:
        """
        Описывает принтер

        :return: 'Принтер средний и цветной'

        Пример:
        >>> printer = Printer('средний', True)
        >>> printer.describe()
        'Принтер средний и цветной'
        """
        printer_description = 'цветной' if self.has_color else 'черно-белый'
        return f'Принтер {self.size} и {printer_description}'

    def add_paper(self, paper: int = 5) -> None:
        """
        Добавление бумаги в принтер

        :param paper: Кол-во добавленных листов бумаги

        Пример:
        >>> printer = Printer('большой', False)
        >>> printer.add_paper()
        5
        """

        if not isinstance(paper, int):
            raise TypeError('Добавляемые листы бумаги должны быть типа int')
        if paper < 0:
            raise ValueError("Добавляемые листы бумаги должны быть положительным числом")

        return paper


# TODO: описать ещё класс
class Flask:
    def __init__(self, gas: str, volume: (int, float), filled_volume: (int, float)):
        """
        Инициализация колбы с газом

        :param gas: Вид газа в колбе (например, 'аргон', 'неон', 'криптон', 'ксенон')
        :param volume: Объем колбы
        :param filled_volume: Объем колбы, заполненной газом

        Пример:
        >>> flask = Flask('аргон', 50, 25.5)
        """

        if gas not in {'аргон', 'неон', 'криптон', 'ксенон'}:
            raise ValueError("Газ должен быть благородным: 'аргон', 'неон', 'криптон', 'ксенон'")
        self.gas = gas
        if not isinstance(volume, (int, float)):
            raise TypeError('Объем колбы должен быть типа int или float')
        if volume <= 0:
            raise ValueError('Объем не может быть отрицательным')
        self.volume = volume

        if not isinstance(filled_volume, (int, float)):
            raise TypeError('Объем, заполненный газом, должен быть типа int или float')
        if filled_volume < 0:
            raise ValueError('Объем, заполненный газом, не может быть отрицательным')
        self.filled_volume = filled_volume

    def is_full_flask(self) -> bool:
        """
        Функция, проверяющая заполнена ли колба газом полностью

        :return: Является ли колба полной
        Пример:
        >>> flask = Flask('криптон', 100, 100)
        >>> flask.is_full_flask()
        True
        """

        return self.filled_volume >= self.volume

    def change_temp(self, new_temp: (int, float) = 5000) -> str:
        """
        Фунция, изменяющая температуру газа в колбе до определенного значения
        :param new_temp: Конечная температура газа в колбе
        :return: Новое значение температуры

        Пример:
        >>> flask = Flask('неон', 150, 67.8)
        >>> flask.change_temp(10000)
        'Температура газа: неон изменена до 10000 градусов Цельсия'
        """
        if not isinstance(new_temp, (int, float)):
            raise TypeError('Новая температура должны быть типа int или float')
        if new_temp <= 0:
            raise ValueError('Новая температура газа не может быть отрицательной или равной нулю')
        return f'Температура газа: {self.gas} изменена до {new_temp} градусов Цельсия'


# TODO: и ещё один
class Pelmeni:
    def __init__(self, quantity: int, meat: str):
        """
        Инициализация пельменей
        :param quantity: Кол-во пельменей в кастрюле
                :param meat: Из чего сделаны пельмени (например, 'свинина', 'говядина', 'курица')

                Пример:
                >>> pelmeni = Pelmeni(25, 'курица')


                """
        if not isinstance(quantity, int):
            raise TypeError('Кол-во пельменей должно быть типа int')
        if quantity < 0:
            raise ValueError('Кол-во пельменей не может быть отрицательным числом')
        self.quantity = quantity

        if meat not in {'свинина', 'говядина', 'курица'}:
            raise ValueError("Пельмени должны быть из: 'свинина', 'говядина', 'курица'")
        self.meat = meat

    def add_pelmeni(self, added_pelmeni: int = 10) -> None:
        """
        Добавление пельменей в кастрюлю

        :param added_pelmeni: Кол-во добавленных пельменей
        >>> pelmeni = Pelmeni(5, 'свинина')
        >>> pelmeni.add_pelmeni(5)
        """
        if not isinstance(added_pelmeni, int):
            raise TypeError('Кол-во добавленных пельменей должно быть типа int')
        if added_pelmeni <= 0:
            raise ValueError('Кол-во добавленных пельменей должно быть положительным числом и не равным нулю')

    def check_price(self, price: (int, float)) -> str:
        """
        Функция, проверяющая стоимость пельменей

        :param price: Цена одного пельменя
        >>> pelmeni = Pelmeni(5, 'говядина')
        >>> pelmeni.check_price(25)
        'Цена 5 пельменей - 125'
        """
        if not isinstance(price, (int, float)):
            raise TypeError('Цена пельменя должна быть типа int или float')
        if price <= 0:
            raise ValueError('Цена пельменя должна быть положительным числом и не равна нулю')
        actual_price = price * self.quantity
        return f'Цена {self.quantity} пельменей - {actual_price}'


if __name__ == "__main__":
    doctest.testmod()
