# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной.

def num_translate_adv(user_string):
    translate_dct = {'one': 'один',
                     'two': 'два',
                     'three': 'три',
                     'four': 'четыре',
                     'five': 'пять',
                     'six': 'шесть',
                     'seven': 'семь',
                     'eight': 'восемь',
                     'nine': 'девять',
                     'ten': 'десять'}
    user_string = user_string.replace(' ', '')
    if user_string == user_string.capitalize():
        return print(translate_dct.get(user_string.lower()).capitalize())
    else:
        return print(translate_dct.get(user_string.lower()))


print('Для выхода введите "1"')
while True:
    user_answer = input('Введите число для перевода: ')
    if user_answer == '1':
        break
    num_translate_adv(user_answer)
