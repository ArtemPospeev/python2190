# * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)для получения информации
# вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

import re

CODING = 'utf=8'
RE_RESP = re.compile(
    r'^((?:[a-z0-9]{1,4}(?:(?:[:]|[.]){1,2})){3,7}[a-z0-9]{1,4})\W{1,5}([[](?:.{1,26})[]])'
    r'\W{1,2}(\w{1,5})\W(.{1,20}).{1,11}(\d{1,3})\W(\d{1,8})'
)


def email_parse(adr):
    if not RE_RESP.match(adr):
        raise ValueError
    return RE_RESP.match(adr).groups()


with open('nginx_logs.txt', 'r', encoding=CODING) as f, open('nginx_logs_parsed.txt', 'w+', encoding=CODING) as f_2:
    for line in f:
        f_2.write(str(email_parse(line)) + '\n')
