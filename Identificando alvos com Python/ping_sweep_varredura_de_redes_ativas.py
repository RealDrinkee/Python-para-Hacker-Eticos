from scapy.all import *

conf.verb = 0

IPs = []

for ip in range(1, 255):
    IPs.append("142.251.132." + str(ip))

pacote = IP(dst=IPs)/ICMP()

ans, unans = sr(pacote, inter=0.1, timeout=1)

print("Hosts ativos:")

for pacoteRecebido in ans:
    print(pacoteRecebido[1][IP].src)