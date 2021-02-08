import atexit
from time import time, strftime, localtime
from datetime import timedelta

# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution


def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))


def log(s, elapsed=None, since_start=False):
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if since_start:
        elapsed = time()-start
    if elapsed:
        print("Elapsed time:", secondsToStr(elapsed))
    print(line)
    print()


def endlog():
    end = time()
    elapsed = end-start
    log("End Program", elapsed)


start = time()
atexit.register(endlog)
log("Start Program")
