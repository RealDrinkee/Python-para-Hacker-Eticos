import socket

dominio = "www.google.com"

with open("brute-force.txt") as arquivo:
    nomes = arquivo.readlines()

for nome in nomes:
    DNS = nome.strip("\n") + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        print("Não foi possível resolver o DNS para " + DNS)