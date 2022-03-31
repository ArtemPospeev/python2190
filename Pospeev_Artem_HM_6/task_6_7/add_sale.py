def add_sale(argv):
    program, summ_sale = argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(summ_sale + '\n')


if __name__ == '__main__':
    import sys

    add_sale(sys.argv)
