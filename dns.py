import socket

dominio = "www.google.com"
nomes = ["www", "mail", "webmail", "ftp", "pop", "ns1", "ns2", "ns3", "intranet", "blog", "smtp", "vpn", "mx", "ns", "ns4", "ns5"]

for nome in nomes:
    dns = f"{nome}.{dominio}"
    try:
        endereco_ip = socket.gethostbyname(dns)
        print(f"{dns}: {endereco_ip}")
    except socket.gaierror:
        print(f"Não foi possível resolver o DNS para {dns}")
