import json
import os
from pathlib import Path

#currentDir = Path(__file__).resolve().parent
currentDir = os.getcwd()
def getConfig(): 
    cacheConfigPath = os.path.join(currentDir, "cacheConfig.json")
    filepoint = open(cacheConfigPath, 'r')
    config = json.load(filepoint)
    return config
