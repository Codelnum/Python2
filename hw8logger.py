import time
from hw8login import true_user

seconds = time.time()
local_time = time.ctime(seconds)

def get_log(local_time, user):
    log_str = f'-({local_time}): {user}'
    return log_str

log_str = get_log(local_time, true_user)