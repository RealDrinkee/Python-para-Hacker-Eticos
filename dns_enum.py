import dns.resolver

dominion = "www.google.com"
registros = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"]

for registro in registros:
    resposta = dns.resolver.query(dominion, registro, raise_on_no_answer=False)
    if resposta.rrset is not None:
        print(resposta.rrset)
