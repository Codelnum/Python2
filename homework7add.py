def add_person(some_string):
    with open('homework7base.txt', 'a') as hw7b:
        hw7b.write(some_string)