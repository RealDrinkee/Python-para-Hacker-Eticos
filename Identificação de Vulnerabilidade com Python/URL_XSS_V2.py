import sys
import requests
import re

def find_all_vulnerabilities(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text

            vulnerabilities = {
                "SQL Injection": [
                    r"'.*\s+OR\s+.*--",
                    r'";\s*SELECT\s*\*',
                    # Adicione outros padrões de SQL Injection famosos aqui
                ],
                "Cross-Site Scripting (XSS)": [
                    r'<\s*script[^>]*>',
                    r'alert\([^)]*\)',
                    # Adicione outros padrões de XSS famosos aqui
                ],
                "Cross-Site Request Forgery (CSRF)": [
                    r'<\s*input[^>]*\stype=["\']?hidden["\']?',
                    r'<\s*form[^>]*\s*action=["\']?https?://',
                    # Adicione outros padrões de CSRF aqui
                ],
                "Injection Attacks": [
                    r'\bor\s*\d*\s*=\s*[0-9\']+',
                    r'union\s+all\s+select',
                    # Adicione outros padrões de Injection Attacks aqui
                ],
                "Autenticação e Gerenciamento de Sessões Fracos": [
                    r"senha\s*=\s*['\"]?",
                    r"sessionid\s*=\s*['\"]?",
                    # Adicione outros padrões de Autenticação e Gerenciamento de Sessões Fracos aqui
                ],
                "Exposição de Dados Sensíveis": [
                    r"senha",
                    r"password",
                    # Adicione outros padrões de Exposição de Dados Sensíveis aqui
                ],
                "Entidades Externas de XML": [
                    r"<!ENTITY",
                    r"SYSTEM",
                    # Adicione outros padrões de Entidades Externas de XML aqui
                ],
                "Quebra de Controle de Acesso": [
                    r"access\s+denied",
                    r"unauthorized",
                    # Adicione outros padrões de Quebra de Controle de Acesso aqui
                ],
                "Configuração Incorreta de Segurança": [
                    r"security\s+misconfiguration",
                    r"config\s+error",
                    # Adicione outros padrões de Configuração Incorreta de Segurança aqui
                ],
                "Deserialização Insegura": [
                    r"java\.io\.ObjectInputStream",
                    r"Object\.deserialize",
                    # Adicione outros padrões de Deserialização Insegura aqui
                ],
                "Utilização de Componentes com Vulnerabilidades Conhecidas": [
                    r"vulnerability",
                    r"exploit",
                    # Adicione outros padrões de Utilização de Componentes com Vulnerabilidades Conhecidas aqui
                ],
                "Log e Monitoramento Ineficientes": [
                    r"log\s+error",
                    r"monitoring\s+failed",
                    # Adicione outros padrões de Log e Monitoramento Ineficientes aqui
                ],
                "Inclusão de Arquivos Arbitrários (LFI e RFI)": [
                    r"include\s*\(.*\)",
                    r"require\s*\(.*\)",
                    # Adicione outros padrões de Inclusão de Arquivos Arbitrários aqui
                ],
                "Segurança do Servidor Web": [
                    r"server\s+error",
                    r"internal\s+server\s+error",
                    # Adicione outros padrões de Segurança do Servidor Web aqui
                ],
                "Segurança de APIs": [
                    r"api\s+key",
                    r"token",
                    # Adicione outros padrões de Segurança de APIs aqui
                ],
                "Injeção de HTML": [
                    r'<\s*img[^>]*\sonerror=["\']?.*["\']?',
                    r'<\s*a[^>]*\shref=["\']?javascript:.*["\']?',
                    # Adicione outros padrões de Injeção de HTML aqui
                ],
                "Exposição de Configuração": [
                    r"config\.js",
                    r"config\.json",
                    # Adicione outros padrões de Exposição de Configuração aqui
                ],
                "Injeção de Comandos": [
                    r";\s*ls",
                    r"|\s*cat\s*/etc/passwd",
                    # Adicione outros padrões de Injeção de Comandos aqui
                ],
                "XML External Entity (XXE) Injection": [
                    r"<!ENTITY",
                    r"SYSTEM",
                    # Adicione outros padrões de XML External Entity (XXE) Injection aqui
                ],
                "Server-Side Request Forgery (SSRF)": [
                    r"file:///etc/passwd",
                    r"127.0.0.1",
                    # Adicione outros padrões de Server-Side Request Forgery (SSRF) aqui
                ],
                "Injeção de Shell": [
                    r";\s*ls",
                    r"|\s*cat\s*/etc/passwd",
                    # Adicione outros padrões de Injeção de Shell aqui
                ],
                "Injeção de Dados (Data Injection)": [
                    r"' OR 1=1 --",
                    r'" OR 1=1 --',
                    # Adicione outros padrões de Injeção de Dados aqui
                ],
                "Escalação de Privilégios (Privilege Escalation)": [
                    r"admin\s+access",
                    r"privileged\s+user",
                    # Adicione outros padrões de Escalação de Privilégios aqui
                ],
                "Cross-Site Script Inclusion (XSSI)": [
                    r'<\s*script[^>]*\ssrc=["\']?http://',
                    r'importScript\(["\']?http://',
                    # Adicione outros padrões de Cross-Site Script Inclusion (XSSI) aqui
                ],
                "Clickjacking": [
                    r'<\s*iframe[^>]*\ssrc=["\']?http://',
                    r'<\s*div[^>]*\sstyle=["\']?position:\s*absolute;',
                    # Adicione outros padrões de Clickjacking aqui
                ],
                "Denial of Service (DoS)": [
                    r".*\s+;\s*fork\s*\(\s*\)",
                    r".*\s+;\s*exec\s*\(\s*\)",
                    # Adicione outros padrões de Denial of Service (DoS) aqui
                ],
                "Buffer Overflow": [
                    r".*\s+;\s*buffer\s+overflow\s*\(",
                    r".*\s+;\s*overflow\s*\(",
                    # Adicione outros padrões de Buffer Overflow aqui
                ],
                "Injeção de Código": [
                    r'eval\([^)]*\)',
                    r'exec\([^)]*\)',
                    # Adicione outros padrões de Injeção de Código aqui
                ],
                "Gerenciamento de Sessão Inseguro": [
                    r"session_start\(\)",
                    r"cookie\s*=\s*session_id\(",
                    # Adicione outros padrões de Gerenciamento de Sessão Inseguro aqui
                ],
                "Exposição de Diretórios": [
                    r"directory\s+listing",
                    r"ls\s*\(",
                    # Adicione outros padrões de Exposição de Diretórios aqui
                ],
                "Vazamento de Informações": [
                    r"leak\s+information",
                    r"expose\s+data",
                    # Adicione outros padrões de Vazamento de Informações aqui
                ],
                "Manipulação de Cookie": [
                    r"setcookie\(",
                    r"$_COOKIE\[",
                    # Adicione outros padrões de Manipulação de Cookie aqui
                ],
                "Execução Remota de Código (RCE)": [
                    r"system\(",
                    r"exec\(",
                    # Adicione outros padrões de Execução Remota de Código (RCE) aqui
                ],
                "Vulnerabilidades de Terceiros (devido a bibliotecas ou plugins desatualizados)": [
                    r"vulnerable\s+library",
                    r"outdated\s+plugin",
                    # Adicione outros padrões de Vulnerabilidades de Terceiros aqui
                ],
                "Falhas de Autenticação": [
                    r"authentication\s+failure",
                    r"login\s+failed",
                    # Adicione outros padrões de Falhas de Autenticação aqui
                ],
                "Redirecionamento Aberto (Open Redirect)": [
                    r'header\(["\']?Location:',
                    r'redirect\(["\']?http://',
                    # Adicione outros padrões de Redirecionamento Aberto aqui
                ],
                "Injeção de NoSQL": [
                    r"noSQL\s+injection",
                    r"query\s*=\s*{\s*.*\s*:\s*{\s*.*\s*:\s*.*\s*}}",
                    # Adicione outros padrões de Injeção de NoSQL aqui
                ],
                "Erros de Configuração de Segurança": [
                    r"security\s+configuration\s+error",
                    r"config\s+misconfigured",
                    # Adicione outros padrões de Erros de Configuração de Segurança aqui
                ],
                "Injeção de Linguagem de Consulta NoSQL (NoSQL Injection)": [
                    r"noSQL\s+query",
                    r"\$where\s*=\s*{.*}",
                    # Adicione outros padrões de Injeção de Linguagem de Consulta NoSQL aqui
                ],
                "Erro de Controle de Acesso": [
                    r"access\s+control\s+error",
                    r"ACL\s+misconfigured",
                    # Adicione outros padrões de Erro de Controle de Acesso aqui
                ],
                "Ataques de Força Bruta": [
                    r"bruteforce\s+attack",
                    r"dictionary\s+attack",
                    # Adicione outros padrões de Ataques de Força Bruta aqui
                ],
                "Erros de Validação de Entrada": [
                    r"input\s+validation\s+error",
                    r"validation\s+failure",
                    # Adicione outros padrões de Erros de Validação de Entrada aqui
                ],
                "Ataques de Man-in-the-Middle (MitM)": [
                    r"man-in-the-middle\s+attack",
                    r"mitm\s+interception",
                    # Adicione outros padrões de Ataques de Man-in-the-Middle aqui
                ],
                "Exposição de Informações de Debugging": [
                    r"debug\s+information\s+exposed",
                    r"traceback\s+revealed",
                    # Adicione outros padrões de Exposição de Informações de Debugging aqui
                ],
                "Ataques de Buffer Overread": [
                    r"buffer\s+overread\s+attack",
                    r"overread\s+vulnerability",
                    # Adicione outros padrões de Ataques de Buffer Overread aqui
                ],
                "Exposição de Informações de Header": [
                    r"header\s+information\s+exposed",
                    r"http\s+response\s+headers",
                    # Adicione outros padrões de Exposição de Informações de Header aqui
                ],
                "Ataques de XML Injection": [
                    r"xml\s+injection",
                    r"<\s*xml[^>]*>",
                    # Adicione outros padrões de Ataques de XML Injection aqui
                ],
                "Vulnerabilidades de Redes Sociais (por meio de APIs sociais)": [
                    r"social\s+media\s+api\s+vulnerability",
                    r"social\s+network\s+security\s+issue",
                ]
                # Adicione verificações para outras vulnerabilidades aqui
            }

            found_vulnerabilities = {}

            for vulnerability, vulnerability_patterns in vulnerabilities.items():
                found_vulnerabilities[vulnerability] = []
                for pattern in vulnerability_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        found_vulnerabilities[vulnerability].append(url)

            return found_vulnerabilities

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

    return {}

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    vulnerabilities = find_all_vulnerabilities(url)

    if vulnerabilities:
        print("Vulnerabilidades encontradas:")
        for vulnerability, urls in vulnerabilities.items():
            if urls:
                print(f"{vulnerability}:")
                for vuln_url in urls:
                    print(f"  - {vuln_url}")
    else:
        print("Não foram encontradas vulnerabilidades conhecidas.")

if __name__ == "__main__":
    main()
