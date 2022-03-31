def show_sales(argv):
    program, *nums = argv
    with open('bakery.csv', encoding='utf-8') as f:
        for ind, line in enumerate(f, start=1):
            if (not nums) or ((len(nums) == 1) and (ind >= int(nums[0]))):
                print(line.strip())
            elif (len(nums) == 2) and (int(nums[0]) <= ind <= int(nums[1])):
                print(line.strip())
                if ind == int(nums[1]):
                    break


if __name__ == '__main__':
    import sys

    show_sales(sys.argv)
