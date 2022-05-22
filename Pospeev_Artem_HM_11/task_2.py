class ZeroDivisionErrorUpd(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a, b = 3, int(input())
    if b == 0:
        raise ZeroDivisionErrorUpd('Деление на ноль недопустимо')
    print(a / b)
except ZeroDivisionErrorUpd as err:
    print(err)

finally:
    print('continue')
