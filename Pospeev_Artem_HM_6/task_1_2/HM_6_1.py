#  Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
#  получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
#
# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
#  из предыдущего задания.

import requests
from pprint import pprint


CODING = 'utf-8'
parsed_list = []
response = requests.get('https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt')
with open('nginx_logs.txt', 'w+', encoding=CODING) as f:
    f.write(response.text)
    f.seek(0)
    for line in f:
        remote_addr = line[:line.index(' ')]
        request_type = line[line.index('"'):line.index(' /')].replace('"', '').replace(' ', '')
        requested_resource = line[line.index(' /'):line.index(' HTTP')].replace(' ', '')
        parsed_list.append((remote_addr, request_type, requested_resource))

print('Вывод первых 10 элементов распаршенного списка:')
pprint(parsed_list[:10])

list_ip = [parsed_list[i][0] for i in range(len(parsed_list))]  # вытаскиваем ip из распаршенного списка
max_count_ip = list_ip.count(list_ip[0])
spamm_ip = list_ip[0]
for ip in set(list_ip):  # проходим по множеству, сравниваем и выискиваем максимум обращений
    if list_ip.count(ip) > max_count_ip:
        max_count_ip, spamm_ip = list_ip.count(ip), ip

print(f'\nIp адрес спаммера: {spamm_ip}\nКоличество обращений: {max_count_ip}')
