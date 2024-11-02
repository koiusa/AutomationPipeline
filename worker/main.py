# Mirror files according to the contents of cacheConfig.json.

import os
import sys
import subprocess
from datetime import datetime as dt
from concurrent.futures import ThreadPoolExecutor

sys.path.append(os.getcwd())
from bin.cache import workingCache as worker

multi = 4
workerdir = os.path.join(os.getcwd(), "worker")

def mirrorring(section, key):
    try:
        fm = section['from']
        to = section['to']
        print(section)
        logsDir = os.path.join(workerdir,f"logs")
        timestamp = dt.now().strftime('%Y%m%d')
        daylydir = os.path.join(logsDir,f"{timestamp}")
        os.makedirs(daylydir, exist_ok=True)
        logs = os.path.join(daylydir,f"logs_{key}.log")
        subprocess.call(f"robocopy {fm} {to} /MIR /COMPRESS /NP /NFL /NDL /LOG+:{logs} /R:1 /W:1 /MT:{multi}")
    except Exception as e:
        print(e)

def main():
    print(workerdir)
    config = worker.getConfig(os.path.join(workerdir, "cacheConfig.json"))

    tpe = ThreadPoolExecutor(max_workers=multi)
    for key in config.keys():
        section = config[key]
        tpe.submit(mirrorring(section,key))

    tpe.shutdown() 
    

if __name__ == "__main__":
    main()
