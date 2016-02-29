This is an experimental driver to generate SMIs.

Tested on kernel 3.17.4-301.fc21.x86_64 running on Fedora 21
This exercises certain SMIs on the Dell servers in the lab. 

=========================================================================================================================================================
To compile and load. If the driver loaded properly, you won't get an error upon doing the insmod command and you'll also see a "/proc/smidriver" file.
Run 'make' from this directory.
As root: "insmod smidriver.ko"
=========================================================================================================================================================
To unload the kernel module:
As root: "rmmod smidriver.ko"
=========================================================================================================================================================
To generate a few SMIs back to back and measure their average latency:
(For short SMIs): "echo 1 > /proc/smidriver"
(For long SMIs):  "echo 2 > /proc/smidriver"
=========================================================================================================================================================
To turn on regularly scheduled SMIs (about once a second)
(For short SMIs): "echo 3 > /proc/smidriver"
(For long SMIs):  "echo 4 > /proc/smidriver"

To turn off regularly scheduled SMIs
"echo 5 > /proc/smidriver"
=========================================================================================================================================================
To check how many SMIs have occurred so far:
"echo 6 > /proc/smidriver"
=========================================================================================================================================================
To get the CPU's timestamp counter value:
"echo 7 > /proc/smidriver"
=========================================================================================================================================================

'dmesg' can display the smidriver printk output.



 
