class Storage:
    def __init__(self, name):
        self.name = name
        self.item_dict = {}

    def add_(self, unit__, position__, value__):

        """Добавление позиций на склад. Формат хранения - словарь в словаре {unit: {position : value}}"""

        if unit__ not in self.item_dict.keys():
            self.item_dict[unit__] = {position__: value__}
            print(f'В подразделении {unit__} создана позиция {position__}, к ней приписано {value__} ед.')
        else:
            if position__ not in self.item_dict[unit__].keys():
                self.item_dict[unit__][position__] = int(value__)
                print(f'В подразделении {unit__} создана позиция {position__}, к ней приписано {value__} ед.')
            else:
                self.item_dict[unit__][position__] += int(value__)
                print(f'В подразделение {unit__} к позиции {position__} добавлено {value__} шт')

    def __str__(self):
        result = ''
        for keys, items_ in self.item_dict.items():
            result += f'---  {keys}  ---\n'
            for key_, item in items_.items():
                result += f'{key_} : {item}\n'
        return result

    def go_to_(self, unit_from_, unit_to_, position_, value_):

        """Перемещение между подразделениями"""

        value_ = int(value_)
        if unit_from_ in self.item_dict.keys() and unit_to_ in self.item_dict.keys():
            if position_ in self.item_dict[unit_from_]:
                if value_ < self.item_dict[unit_from_][position_]:
                    self.item_dict[unit_from_][position_] -= value_
                    self.add_(unit_to_, position_, value_)
                else:
                    print('Ведено значение превышает остаток по этой позиции в подразделении- отправителе')
            else:
                print('Такой позиции нет у подразделения- отправителя')
        else:
            print('Допустили ошибку в названии подразделений/ такого подразделения нет')


class OfficeEquip:
    def __init__(self, brand_name, model):
        self.brand_name = brand_name
        self.model = model

    def __str__(self):
        return f'{self.brand_name}_{self.model}'

    def show_info_(self):  
        return_str = ''
        for keys, item in self.__dict__.items():
            if keys != 'attributes':
                return_str += f'{keys} : {item}\n'
        return return_str

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __hash__(self):
        return hash(str(self))


# Структура и методы всех классов +- одинаковые. Для ознакомления можно посмотреть Scanner, там меньше всего кода
class Printer(OfficeEquip):
    def __init__(self, brand_name, model, speed_printing, wifi, color_number, format_printing):
        super(Printer, self).__init__(brand_name, model)
        self.speed_printing = speed_printing  # int ( стр/ м )
        self.wifi = wifi  # bool (есть/ нет)
        self.color_number = color_number  # int (1, 4, 5 и т.д.)
        self.format_printing = format_printing  # str (а4, a3 и пр)

    @staticmethod
    def init_print():  # Инициализация класса. Метод у каждого класса для его определения внутри блока основной логики
        br_name = input('Введите название бренда печатающего устройства: ')
        model = input('Введите модель печатающего устройства: ')
        answer = input('Хотите ли вы заполнить опциональные параметры? Для продолжения- любой символ\n'
                       'Для выхода введите "stop" cейчас или далее на любом этапе.\n'
                       'В случае их отсутствия выставляются значения None\n')
        speed_print, wifi_, color_number, format_printing = None, None, None, None
        if answer != 'stop':
            while True:
                speed_print = input('Введите скорость печати (стр/м):\n')
                if speed_print.lower() == 'stop':
                    break
                elif not speed_print.isnumeric():
                    print('Вы ввели не число. Попробуйте ещё раз')
                    continue
                else:
                    speed_print = int(speed_print)
                wifi_ = input('Наличие Wifi? Да, нет: ')
                if wifi_.lower().strip() == 'stop':
                    break
                elif wifi_.strip().lower() == 'да':
                    wifi_ = True
                elif wifi_.strip().lower() == 'нет':
                    wifi_ = None
                else:
                    print('Некорректно введен ответ, присвоено значение None')
                    wifi_ = None
                color_number = input('Введите количество цветов (1 - чб, остальное ситуативно):\n')
                if color_number.lower().strip() == 'stop':
                    break
                elif not color_number.isnumeric():
                    print('Введено не число. Присвоено значение None')
                    color_number = None
                else:
                    color_number = int(color_number)
                format_printing = input('Введите максимально-допустимый формат бумаги (а4, а3 и пр):\n')
                if format_printing.lower().strip() == 'stop':
                    format_printing = None
                break
        return [br_name, model, speed_print, wifi_, color_number, format_printing]
    # Возвращаем список для распаковки и инициализации с его помощью нового экземпляра класса


class Scanner(OfficeEquip):
    def __init__(self, brand_name, model, max_format_scanning, wifi):
        super(Scanner, self).__init__(brand_name, model)
        self.max_format_scanning = max_format_scanning  # str (a4, a3 и пр)
        self.wifi = wifi  # bool

    @staticmethod
    def init_scan():
        br_name = input('Введите название бренда сканера: ')
        model = input('Введите модель сканера: ')
        answer = input('Хотите ли вы заполнить опциональные параметры? Для продолжения- любой символ\n'
                       'Для выхода введите "stop" cейчас или далее на любом этапе.\n'
                       'В случае их отсутствия выставляются значения None\n')
        max_form_scan, wifi = None, None
        if answer.strip().lower() != 'stop':
            while True:
                max_form_scan = input('Введите максимальный формат для сканирования (а4, а3 и пр):\n')
                if max_form_scan.strip().lower() == 'stop':
                    break
                wifi = input('Наличие Wifi? Да, нет: ')
                if wifi.lower().strip() == 'stop':
                    break
                elif wifi.strip().lower() == 'да':
                    wifi = True
                elif wifi.strip().lower() == 'нет':
                    wifi = None
                else:
                    print('Некорректно введен ответ, присвоено значение None')
                    wifi = None
                break
        return [br_name, model, max_form_scan, wifi]


class MultifunctionalDevice(Printer):
    # По-хорошему бы наследоваться от Printer + Scanner, но у меня не получилось красиво сделать :(
    def __init__(self, brand_name, model, speed_printing, wifi, color_number, format_printing, max_format_scanning):
        super(MultifunctionalDevice, self).__init__(brand_name, model, speed_printing, wifi, color_number,
                                                    format_printing)
        self.max_format_scanning = max_format_scanning

    @staticmethod
    def init_multifunctional():
        # Тут тоже не совсем красиво получается. Если отказаться от заполнения доп параметров в init_print(),
        # все равно про сканнер спросит. Не совсем красиво, но менять init в сканнера уже не очень хотелось
        lst_return = Printer.init_print()
        max_form_scan = input('Введите формат сканера (а4, а3 и пр):\n')
        if max_form_scan.strip().lower() == 'stop':
            max_form_scan = None
        lst_return.append(max_form_scan)
        return lst_return


class Computer(OfficeEquip):
    def __init__(self, brand_name, model, proc, ram, operation_sys):
        super(Computer, self).__init__(brand_name, model)
        self.proc = proc  # str (проц)
        self.ram = ram  # int (4, 8, 16)
        self.operation_sys = operation_sys  # str (если установлена ОС)/ None, если нет

    @staticmethod
    def init_comp():
        br_name = input('Введите название бренда ПК: ')
        model = input('Введите модель: ')
        answer = input('Хотите ли вы заполнить опциональные параметры? Для продолжения- любой символ\n'
                       'Для выхода введите "stop" cейчас или далее на любом этапе.\n'
                       'В случае их отсутствия выставляются значения None\n')
        proc, ram, operation_sys = None, None, None
        if answer.strip().lower() != 'stop':
            while True:
                proc = input('Введите модель процессора:\n')
                if proc.strip().lower() == 'stop':
                    break
                ram = input('Введите объём оперативной памяти - число - (1, 2, 4 и пр):\n')
                if ram.strip().lower() == 'stop':
                    break
                elif not ram.isnumeric():
                    print('Вы ввели не число, записано None')
                    ram = None
                else:
                    ram = int(ram)
                operation_sys = input('Введите модель предустановленной ОС. Enter, если ОС нет\n')
                if operation_sys == '':
                    operation_sys = None
                break
        return [br_name, model, proc, ram, operation_sys]


my_store = Storage(input('Введите название склада:\n'))
"""Просто для демонстрации работоспособности вручную заполнил чем-то склад, т.к. через логику это очень долго"""
epson_2100 = MultifunctionalDevice('Epson', 'xp2100', '30', 'да', 4, 'a4', 'a4')
epson_121 = Printer('Epson', '121', '40', 'нет', 4, 'a4')
pc_1 = Computer('HP', 'pavilion_133', 'proc_name', 16, 'win10')
scan_1 = Scanner('Canon', 'CanoScan', 'a3', 'да')
my_store.add_('Склад', epson_121, 20)
my_store.add_('Склад', scan_1, 15)
my_store.add_('Бухгалтерия', pc_1, 35)
my_store.add_('Бухгалтерия', epson_2100, 30)
print(f'Текущее состояния склада(для тестовой работы) - \n{my_store}')


while True:
    user_action = input('Введите действие, которое хотите совершить со складом\n1. Завести наименование на склад'
                        '\n2. Переместить позиции по подразделениям\n'
                        '3. Добавить или списать единицы к уже существующему наименованию\n'
                        '4. Показать полную информацию по позиции\n'
                        '5. Вывести текущее состояние склада\n'
                        'Введите соответствующую цифру:\n')
    if user_action.isnumeric() and 0 < int(user_action) < 6:
        user_action = int(user_action)
        if user_action == 1:
            unit = input('Введите название подразделения, куда заводим товар:\n')
            while True:
                name_pos = input('Какую единицу техники хотите добавить на склад? Введите соответствующую цифру:\n' +
                                 '1. Принтер\n2. Cканер\n3. МФУ\n4. Компьютер\n')
                if name_pos.isnumeric() and 0 < int(name_pos) < 5:
                    name_pos = int(name_pos)
                    break
                else:
                    print('Такой позиции нет в списке, попробуйте ещё раз')
            while True:
                value = input('Введите количество:\n')
                if value.isnumeric():
                    value = int(value)
                    break
                else:
                    print('Вы ввели не число, попробуйте ещё раз..')
            if name_pos == 1:
                my_store.add_(unit, Printer(*Printer.init_print()), value)
            elif name_pos == 2:
                my_store.add_(unit, Scanner(*Scanner.init_scan()), value)
            elif name_pos == 3:
                my_store.add_(unit, MultifunctionalDevice(*MultifunctionalDevice.init_multifunctional()), value)
            elif name_pos == 4:
                my_store.add_(unit, Computer(*Computer.init_comp()), value)
        elif user_action == 2:
            print(my_store)
            unit_from = input('Введите подразделение, откуда перемещаем:\n')
            unit_to = input('Введите подразделение, куда перемещаем:\n')
            position = input('Введите название позиции (точно так же, как в сообщении выше):\n')
            value = input('Введите количество, которое нужно переместить:\n')
            my_store.go_to_(unit_from, unit_to, position, value)
        elif user_action == 3:
            while True:
                print(my_store)
                unit = input('Введите название подразделения:\n')
                if unit in my_store.item_dict.keys():
                    break
                else:
                    print('Вы ввели неверное название подразделения, попробуйте ещё раз')
            while True:
                action = input('Что вы хотите сделать?\n1. Добавить единицы к существующий номеклатуре\n'
                               '2. Списать единицы у существующей номеклатуры\n')
                if action.strip() == '1' or action.strip() == '2':
                    action = int(action)
                    break
                else:
                    print('Такое действие недопустимо. Введите 1 или 2')
            while True:
                position = input('Введите название позиции, к которой нужно добавить единицы:\n' if action == 1 else
                                 'Введите название позиции, c которой нужно списать единицы:\n')
                if position in my_store.item_dict[unit].keys():
                    break
                else:
                    print('Вы ввели неверное название позиции, попробуйте ещё раз..')
            while True:
                value = input('Введите количество:\n')
                if (action == 1 and value.isnumeric() and int(value) > 0) or \
                        (action == 2 and value.isnumeric() and int(value) >= my_store.item_dict[unit][position]):
                    break
                else:
                    print(
                        r'Вы ввели число меньше нуля\не число, попробуйте ещё раз' if action == 1
                        else r'Вы ввели число меньше нуля\не число\количество превышает остаток на складе')
            if action == 1:
                my_store.item_dict[unit][position] += int(value)
                print(f'В подразделение {unit} к позиции {position} добавлено {value} ед.\nНа складе теперь '
                      f'{my_store.item_dict[unit][position]} ед.')
            else:
                my_store.item_dict[unit][position] -= int(value)
                if my_store.item_dict[unit][position] != 0:
                    print(f'В подразделении {unit} у позиции {position} списано {value} ед.\nНа складе теперь '
                          f'{my_store.item_dict[unit][position]} ед.')
                else:
                    print(f'В подразделении {unit} у позиции {position} списано {value} ед.\n')
                    action = input(f'У {position} не осталось единиц. Желаете ли вы удалить её? y|n\n')
                    if action.lower() == 'y':
                        del my_store.item_dict[unit][position]
        elif user_action == 4:
            while True:
                print(my_store)
                pos_for_info = input('Введите название позиции, по которой требуется получить информацию:\n')
                for item_ in my_store.item_dict.values():
                    if pos_for_info in item_.keys():
                        for key in item_.keys():
                            if key == pos_for_info:
                                print(key.show_info_())
                                break
        elif user_action == 5:
            print(my_store)
    else:
        print(r'Вы ввели не число\ такого пункта в меню нет, попробуй ещё раз')
