# Send and receive data using TCP and UDP
# Use raw sockets to access lower-level networking information (IP, ICMP headers)

# Building UDP host discovery tool
# Sniffer discovers hosts on target network
# Send UDp datagram to closed port on host, host sends back ICMP

# Create socket object and determine which platform to run on
# Set up raw socket sniffer, read single packet, quit

import socket
import os
# Host to liston on (changes)
HOST = '127.0.0.1'

def main():
    # Create raw socket, bind to public interface
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    
    # Windows allows sniffing all incoming packets, Linux forces specify sniffing ICMP packets
    # Using promiscuous mode (requires admin privileges) allows sniff all packets the network card sees
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    # Include IP header in the capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # Determine if Windows is used, if so, send IOCTL to network card driver to enable promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    # Read one packet and print entire raw packet
    print(sniffer.recvfrom(65565))

    # If on Windows, turn off promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RVCALL, socket.RVCALL_OFF)

if __name__ == '__main__':
    main()