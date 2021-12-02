#!/usr/bin/python3

DOC = """

Problem. Give a ping name e.g. P9_14 you would like to know its 
         associated GPIO file in sysfs. 

Solution. 
$> pinNameToGPIO.py P9_14
or
$> pinNameToGPIO.py P9.14

CAVEAT. If a pin PX_Y must be already defined to be a GPIO pin to be found.

"""


import sys 
import os 

# . where to look fro gpio files 
BASE_DIR = '/sys/class/gpio';

# . the first argument is needed, abort if absent  
if len(sys.argv) < 2:
    print("Error, first argument is needed, a pin name, e.g. P9.11 or P9_11.")
    sys.exit(1)

# . the pin name is the first argument, allow some variabiliy in input: P9_14 = P9.14 = p9.14
PIN_NAME = sys.argv[1]
# . dot is admitted instead of underscore 
PIN_NAME = PIN_NAME.replace('.', '_', 1).strip()
# . 'P' case is irrelevant
PIN_NAME = PIN_NAME.replace('p', 'P', 1).strip()



# all files in like /sys/class/gpio/gpio*
allFiles = os.listdir(BASE_DIR)
allFiles = [x for x in allFiles if 'gpio' in x]

for f in allFiles:
    fullPath = BASE_DIR + '/' + f + '/label'
    text = open(fullPath, 'r').read().strip()
    # print(text)
    if PIN_NAME in text :
       print(fullPath.replace('/label','',1))
       break 
    



