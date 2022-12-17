def export_list(filename):
    with open('homework7base.txt', 'r') as hw7print:
        text = hw7print.read()
    with open(f'{filename}', 'w+') as new_list:
        new_list.write(text)
