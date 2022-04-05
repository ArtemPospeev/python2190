# Task_1
# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
# почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
# Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл
# в данном случае использовать функцию re.compile()?


import re

RE_EMAIL = re.compile(r'^([a-z0-9]+)[@]([a-z0-9]+[.][a-z]{2,3})')


def email_parse(adress):
    parsed_dict = {}
    adress = adress.lower()
    if not RE_EMAIL.match(adress):  # проверка для вызова исключения
        msg = f'wrong email: {adress}'
        raise ValueError(msg)
    parsed_dict['username'] = RE_EMAIL.match(adress).groups()[0]
    parsed_dict['domain'] = RE_EMAIL.match(adress).groups()[1]
    return parsed_dict


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))  # исключение ValueError
