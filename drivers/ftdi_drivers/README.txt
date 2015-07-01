setup:
1. # make
2. # sudo cp ftdi_sio.ko /lib/modules/$(uname -r)/kernel/drivers/usb/serial 
3. Using the preferred text editor, add the following line to the /etc/modules file:
    ftdi_sio
4. reboot
5. # sudo cp usb.ids /var/lib/usbutils/
5. It is not possible to access the Virtual COM port in Ubuntu until the “brltty” port is removed. This is done
as follows:
# sudo apt-get remove brltty


