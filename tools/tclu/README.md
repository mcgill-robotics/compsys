# Teensy Command Line Uploader

This tool is a fork of PJRC's
[teensy_loader_cli](https://github.com/PaulStoffregen/teensy_loader_cli),
 Teensy Loader Command Line Interface, to allow command line code upload to
 specific Teensy by Specifying the port path.

## Dependencies

This tool has two dependecies, 'libusb' and 'libudev', you can get them by
running:

'''bash
sudo apt-get install libusb-dev libudev-dev
'''

## Compilation

Simply run 'make' to compile the code after installing the dependencies.

## Usage

### Explanation
'tclu [--mcu=<MCU>] [--port=</dev/ttyACM0>] [-w] [-r] [-s] [-n] [-v] <file.hex>'

* '--mcu' : MCU of the teensy to be uploaded. use 'tclu --list-mcus' for a list
of suppoted MCUs.
* '--port' : Serial port where the specific Teensy is mounted. A soft reboot will
be performed to put the Teensy at that port into bootloader mode.
* '-w' : Wait Teensy to appear. This option is used in junction with manually
 resetting the Teensy into bootloader mode.
* '-r' : Use hard reboot if there is no Teensy in bootloader mode.
'-s' : Use soft reboot if there is no Teensy in bootloader mode,
only work with Teensy 3.0 or above.
* '-n' : No reboot after programming.
* '-v' : Verbose mode.

### Sample usage:

'''bash
./tclu --port=/dev/ttyACM0 blink_fast.hex
'''

### Sample output:

'''
Teensy Command Line Uploader, McGill Robotics Mod

tclu: Reading Hex file: blink_slow.hex
	Size: 12288 bytes, 4.7% usage

tclu: Soft reboot performed...
	Waiting for Teensy to reappear...

tclu: Programming Teensy...

tclu done.  Thank you.
'''
