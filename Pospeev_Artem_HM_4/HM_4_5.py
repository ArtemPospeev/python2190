import requests
from datetime import datetime


def currency_rates(argv):
    program, *input_value = argv
    input_value = str(*input_value)  # для исключений по неверному типу выходных данных
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    str_response = str(response.text)
    response_header = str(response.headers)
    response_header = response_header[response_header.index('Expires='):response_header.index('GMT')]. \
        replace('Expires=', '').replace('-', ' ')  # вытаскиваем время в строке из заголовка
    dateFormatter = '%a, %d %b %Y %H:%M:%S'  # формат даты
    output_date = datetime.strptime(response_header[:-1], dateFormatter)
    if input_value.upper() in str_response:
        rslt_value = str_response[str_response.index(input_value.upper()):]
        rslt_value = rslt_value[rslt_value.find('<Value>'):rslt_value.index('</Value>')]. \
            replace('<Value>', '').replace(',', '.')
        return_str = f'Время запроса: {output_date} \nКурс: {float(rslt_value)}'
    else:
        return_str = f'Время запроса: {output_date} \nКурс: {None}'
    return return_str


if __name__ == '__main__':
    import sys

    exit(currency_rates(sys.argv))
