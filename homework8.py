from hw8login import true_user, input_num



if input_num == 1:
    from hw8teachers_list import teach_dict
    from hw8teach_menu import teachers_choice
    lesson = teach_dict[f'{true_user}']
    teachers_choice(lesson)
else:
    from hw8stud_menu  import select, les
    select(les)