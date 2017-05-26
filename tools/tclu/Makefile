CC ?= gcc
CFLAGS ?= -O2 -Wall
LIB ?= -lusb -ludev -lsysfs
tclu: tclu.c
	$(CC) $(CFLAGS) -s -DUSE_LIBUSB -o tclu tclu.c $(LIB)

clean:
	rm -f tclu
