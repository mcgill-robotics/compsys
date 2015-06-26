setup:

1.
# make

2.
# cp ftdi_sio.ko /lib/modules/$(uname –r)/kernel/drivers/usb/serial 

3.
Using the preferred text editor, add the following line to the /etc/modules file:

ftdi_sio

4.
reboot

5.
It is not possible to access the Virtual COM port in Ubuntu until the “brltty” port is removed. This is done
as follows:

# sudo apt-get remove brltty


Note:
these files are modified versions
of the ones associated with linux
kernel 3.13.*
found here:

http://lxr.free-electrons.com/source/drivers/usb/serial/ftdi_sio.c?v=3.13
http://lxr.free-electrons.com/source/drivers/usb/serial/ftdi_sio.h?v=3.13
http://lxr.free-electrons.com/source/drivers/usb/serial/ftdi_sio_ids.h?v=3.13

they may need to be modified if
used with a different kernel version