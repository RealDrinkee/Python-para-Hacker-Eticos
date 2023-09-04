import sys
try:
    from scapy.all import *
except:
    sys.exit("[!] Por favor, instale a biblioteca scapy com o comando: pip3 install scapy")

conf.verb = 0

IPs = []

for ip in range(1, 255):
    IPs.append("142.251.132." + str(ip))

pacoteARP = Ether()/ARP(pdst=IPs, hwdst='ff:ff:ff:ff:ff:ff')
ans, unans = srp(pacoteARP, inter=0.1, timeout=1)

print("IP\t\tMAC")
for pacoteRecebido in ans:
    print(pacoteRecebido[1][ARP].psrc, "\t", pacoteRecebido[1][ARP].hwsrc)