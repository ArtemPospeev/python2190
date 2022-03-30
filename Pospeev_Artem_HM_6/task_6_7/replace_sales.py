def replace_sales(argv):
    program, *nums = argv
    line_count = 0
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        with open('bakery.csv', 'r+', encoding='utf-8') as f_2:
            f.seek(0)
            for ind, line in enumerate(f, start=1):
                line_count += 1
                if line.isspace():
                    f_2.write(line.replace('\n', ''))
                if int(nums[0]) == ind:
                    if len(line) > len(nums[1]):
                        counter = len(line) - len(nums[1])
                        for _ in range(counter):
                            nums[1] += ' '
                    f_2.write(nums[1] + '\n')
                else:
                    f_2.write(line)
            if (int(nums[0]) < 0) or (int(nums[0]) > line_count):
                exit('Not in range')


if __name__ == '__main__':
    import sys

    replace_sales(sys.argv)
