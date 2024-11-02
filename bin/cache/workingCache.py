import json
import os
from pathlib import Path

#currentDir = Path(__file__).resolve().parent
currentDir = os.getcwd()
def getConfig(conf) -> dict: 
    #cacheConfigPath = os.path.join(currentDir, "cacheConfig.json")
    cacheConfigPath = conf 
    filepoint = open(cacheConfigPath, 'r')
    config = json.load(filepoint)
    print(json.dumps(config, indent=4))
    return config
