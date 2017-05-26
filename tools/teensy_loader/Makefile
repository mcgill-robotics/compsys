CC ?= gcc
CFLAGS ?= -O2 -Wall
LIB ?= -lusb -ludev -lsysfs
teensy_loader: teensy_loader.c
	$(CC) $(CFLAGS) -s -DUSE_LIBUSB -o teensy_loader teensy_loader.c $(LIB)

clean:
	rm -f teensy_loader
