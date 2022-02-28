duration, sec, minuts, hours, days = int(input()), 0, 0, 0, 0
while duration // 60 != 0:  # пока секунд > 60
    if duration > 60: # если секунд > 60, то добавляем 1 минуту, отнимаем 60 сек
        minuts += 1
        duration -= 60
    if minuts == 60: # аналогично с минутами для часов
        minuts = 0
        hours += 1
    if hours == 24: # аналогично для суток
        hours = 0
        days += 1
sec = duration # после цикла записываем остаток в секунды

if days != 0:
    print(days, 'дн', hours, 'час', minuts, 'мин', sec, 'сек')
elif (days == 0) and (hours != 0):
    print(hours, 'час', minuts, 'мин', sec, 'сек')
elif (days == 0) and (hours == 0) and (minuts != 0):
    print(minuts, 'мин', sec, 'сек')
else:
    print(sec, 'сек')