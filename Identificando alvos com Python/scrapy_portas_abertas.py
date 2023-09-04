from scapy.all import *

ip = "142.251.132.46"
dst_port = [21, 22, 23, 25, 80, 443, 8080]
open_ports = []

headers = IP(dst=ip) / TCP(dport=dst_port, flags="S")

answers, unanswers = sr(headers, timeout=10)

for sent_packet, received_packet in answers:
    if received_packet.haslayer(TCP) and received_packet[TCP].flags & 0x12:  # Check if SYN/ACK is set
        print(f"Port {received_packet[TCP].sport} is open")
        open_ports.append(received_packet[TCP].sport)

print("Open ports:", open_ports)
