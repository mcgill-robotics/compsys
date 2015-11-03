CC ?= gcc
CFLAGS ?= -O2 -Wall
teensy_loader: teensy_loader.c
	$(CC) $(CFLAGS) -s -DUSE_LIBUSB -o teensy_loader teensy_loader.c -lusb

clean:
	rm -f teensy_loader
