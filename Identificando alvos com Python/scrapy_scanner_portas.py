import sys
try:
    from scapy.all import *
except:
    sys.exit("[!] Por favor, instale a biblioteca scapy com o comando: pip3 install scapy")

conf.verb = 0

portas = [1,21, 22, 23, 25, 80, 443, 8080, 8081, 8082, 8083, 8084, 8085, 8001]

pacoteIP = IP(dst = "142.251.132.46")
pacoteTCP = TCP(dport = portas, flags = "S")
pacote = pacoteIP/pacoteTCP

ans, unans = sr(pacote, inter=0.1, timeout=1)

print("Portas\tEstado")
for pacoteRecebido in ans:
    print(pacoteRecebido[1][TCP].sport, "\t", pacoteRecebido[1][TCP].sprintf("%flags%"))