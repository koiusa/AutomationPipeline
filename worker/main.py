import os
import sys
import importlib

sys.path.append(os.getcwd())
from bin.cache import workingCache as worker

def main():
    config = worker.getConfig();
    print(config)

if __name__ == "__main__":
    main()
