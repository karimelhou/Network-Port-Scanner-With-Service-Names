# Network Port Scanner with Service Names

This program is an updated version of a basic network port scanner. In addition to returning the port numbers of any open ports, this version also returns the corresponding service names for each open port.

## Requirements

Python 3.x <br>
Unix-based system

## Usage

To use this program, you must provide the IP address of the target host you want to scan, and the range of ports you want to scan.

The program will return a list of tuples, where each tuple contains the port number and the corresponding service name for any open ports.

## Note

This program is designed to run on Unix-based systems and uses the socket and getservbyport modules to retrieve the service names for open ports. If you are using a different operating system, you may need to modify the code to work on your system.
