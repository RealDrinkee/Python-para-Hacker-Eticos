import socket

dominio = "dominio.com"
registros = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"]

for registro in registros:
    try:
        if registro == "A":
            resposta = socket.gethostbyname(dominio)
            print(f"{registro}: {resposta}")
        elif registro == "AAAA":
            resposta = socket.getaddrinfo(dominio, None, socket.AF_INET6)
            for resultado in resposta:
                endereco_ipv6 = resultado[4][0]
                print(f"{registro}: {endereco_ipv6}")
        else:
            print(f"Consulta DNS não suportada para o registro {registro}")
    except socket.gaierror as e:
        print(f"Erro ao consultar {registro}: {e}")
    except Exception as e:
        print(f"Erro desconhecido ao consultar {registro}: {e}")
