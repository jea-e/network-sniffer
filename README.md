# network-sniffer

Send and receive data using TCP and UDP
Use raw sockets to access lower-level networking information (IP, ICMP headers)

Building UDP host discovery tool
Sniffer discovers hosts on target network
Send UDP datagram to closed port on host, host sends back ICMP

Create socket object and determine which platform to run on
Set up raw socket sniffer, read single packet, quit
