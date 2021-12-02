# pinNameToGPIO
BeagleBoard. Find the GPIO file associated to a given pin-name, like P9_14

## Mini documentation

### Problem description 

It often happens that we want to use a pin as a digital input/output pin, that is a **gpio**. 
To do so first you need to say to the *beagleboard* the pin is a GPIO. You can do it do using **config-pin** then,
you need to know which file in the filesystem has been associated to the GPIO, that is, you need to establish the  `XXX` value 
in `/sys/class/gpio/gpioXXX`. There is a formula to do that, but its is different between the *BB-Black* and
the *BB-AI* also, it does not always work: e.g. in *BB-AI* for `P9_11` to me it fails. Therefore I give 
us this script which should solve the problem once and for all.

### Example 

* We know pin `P9_14` is set to gpio, what is its associated file in *sysfs* ?
* You run:
```
$> pinNameToGPIO.py P9_14
```
* In my system I get as output `/sys/class/gpio/gpio121`, your output may be different.
* If you get no output it means the associated file was not found.
* You can write the pin name as `P9_14` or `P9.14` and it is **case insensitive**.

### Tested working in  
* 02-dec-2021. BB-AI, BeagleBoard.org Debian Buster IoT Image 2021-10-01, Linux BB-AI-1 4.19.94-ti-r68 #1buster

**ATTENTION !!**
* The *BeagleBoard* world moves fast, always check:
  *  Your board name
  *  Your operating system version  

### Changelog
* 02-dec-10 - improving the Readme
