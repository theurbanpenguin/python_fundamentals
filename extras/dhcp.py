#!/usr/bin/env python3
# sudo apt install -y python3-venv
# cd venv ; python3 -m venv dhcp
# pip3 install scapy
from scapy.all import *

conf.checkIPaddr = False  # Disabling the IP address checking

# Building the DISCOVER packet

# Making an Ethernet packet
DHCP_DISCOVER = Ether(dst='ff:ff:ff:ff:ff:ff', src=RandMAC(), type=0x0800) \
            / IP(src='0.0.0.0', dst='255.255.255.255') \
            / UDP(dport=67, sport=68) \
            / BOOTP(op=1, chaddr=RandMAC()) \
            / DHCP(options=[('message-type', 'discover'), ('end')])

# Sending the crafted packet in layer 2 once using the "eth0" interface
answered = srp1(DHCP_DISCOVER, iface='eth0', verbose=0)

if answered:
    if DHCP in answered:
        offered_ip = answered[BOOTP].yiaddr
        print(f"Offered IP Address: {offered_ip}")
    else:
        print("No DHCP Offer received.")
else:
    print("No response received."