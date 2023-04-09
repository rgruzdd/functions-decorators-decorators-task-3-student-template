import time

log_file = open("logfile.txt", 'a+')


def log(fn):
    def wrapper(*args, **kwargs):
        global log_file
        time1 = time.time()
        result = fn(*args, **kwargs)
        time2 = time.time()
        time3 = time2 - time1
        time_str = str(time3) + ' sec.'
        string = str(fn.__name__) + '; args: a=' + str(result[0]) + ', b=' + str(result[1]) + '; kwargs: c=' + str(result[2]) + '; ' +'execution time: '
        log_file.write(string + time_str)
        log_file.close()
        return result

    return wrapper

@log
def foo(a, b, c):
    return a, b, c

foo(1, 2, c=3)
