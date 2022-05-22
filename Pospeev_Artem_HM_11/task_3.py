class NoneInt(Exception):
    def __init__(self, txt):
        self.txt = txt


result_lst = []
while True:
    inp_num = input('Введите число: ')
    if inp_num == 'stop':
        print(result_lst)
        break
    try:
        if inp_num.isnumeric() or (inp_num.startswith('-') and inp_num[1:].isnumeric()):
            result_lst.append(inp_num)
        else:
            raise NoneInt('Вы ввели не число')
    except NoneInt as err:
        print(err)
        continue





