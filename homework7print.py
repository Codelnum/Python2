
def print_list(args):
    if args == 1:
        with open('homework7base.txt', 'r') as hw7print:
            text = hw7print.readline(0)
            for line in hw7print:
                print(line)
    elif args == 2:
        with open('homework7base.txt', 'r') as hw7print:
            text = hw7print.readlines()
            print(text)
    else:
        print('wrong args for print_list')
