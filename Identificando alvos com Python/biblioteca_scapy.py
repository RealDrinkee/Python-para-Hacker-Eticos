from scapy.all import *


ip = "142.251.132.46"
icmp = IP(dst=ip)/ICMP()
resp = sr1(icmp, timeout=10)

if resp == None:
    print("Host " + ip + " está inativo ou não responde.")
else:
    print("Host " + ip + " está acordado e respondendo.")