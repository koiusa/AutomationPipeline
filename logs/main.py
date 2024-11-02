# delete old logs

import os
import sys
import shutil
import time

sys.setrecursionlimit(10000)
th_date = 7
old_dt = time.time() - th_date * 86400
workerdir = os.path.join(os.getcwd(), "worker")

def main():
    logsDir = os.path.join(workerdir,f"logs")
    print(logsDir)
    for curdir, dirs, files in os.walk(logsDir):
        for dir in dirs:
            target = os.path.join(curdir, dir)
            if os.path.getmtime(target) < old_dt:
                print(target)
                shutil.rmtree(target, ignore_errors=True)

if __name__ == "__main__":
    main()