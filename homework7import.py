def import_list(file_name):
    import_file = open(f"{file_name}",'r')
    merge_file = open("homework7base.txt",'a')
    merge_file.write(import_file.read())