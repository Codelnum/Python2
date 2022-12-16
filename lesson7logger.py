import time
seconds = time.time()
local_time = time.ctime(seconds)

def save_log(some_string):
    file = open('lesson7log.txt', 'a')
    file.write(f'{some_string} ({local_time})\n')
    file.close()