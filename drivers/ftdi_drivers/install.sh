#!/bin/bash
echo "make FTDI driver"
make
echo "Copying driver to kernal modules"
sudo cp -v ftdi_sio.ko /lib/modules/$(uname -r)/kernel/drivers/usb/serial
echo "Copying usb.ids"
sudo cp usb.ids /var/lib/usbutils/
echo "Please add ftdi_sio to your /etc/modules files manually!"
echo "done"
