# pinNameToGPIO
BeagleBorad. Find the GPIO file associated to a given pin-name, like P9_14

## Mini documentation
Taken from the source file 
```
Problem. Give a ping name e.g. P9_14 you would like to know its 
         associated GPIO file in sysfs. 

Solution. 
$> pinNameToGPIO.py P9_14
/sys/class/gpio/gpio241
or
$> pinNameToGPIO.py P9.14
/sys/class/gpio/gpio241

CAVEAT. If a pin PX_Y must be already defined to be a GPIO pin to be found.
```
