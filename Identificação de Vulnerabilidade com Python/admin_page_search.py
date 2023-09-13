import requests
from colorama import Fore, init
import random
import argparse

# Initialize Colorama
init(autoreset=True)

def search_panel(url):
    payload = [
        # English
        "/admin/", "/administrator/", "/admin1/", "/admin2/", "/admin3/", "/admin4/", "/admin5/",
        "/usuarios/", "/usuario/", "/moderator/", "/webadmin/", "/adminarea/", "/bb-admin/",
        "/adminLogin/", "/admin_area/", "/panel-administration/", "/instadmin/", "/memberadmin/",
        "/administratorlogin/", "/adm/",
        "/admin/account/", "/admin/index/", "/admin/login/", "/admin/admin/",
        "/admin_area/admin/", "/admin_area/login/", "/siteadmin/login/", "/siteadmin/index/",
        "/admin_area/index/", "/bb-admin/index/", "/bb-admin/login/", "/bb-admin/admin/",
        "/admin/home/", "/admin/controlpanel/", "/admin/admin_login/",
        "/admin_login/", "/administrator/account/", "/administrator/",
        "/pages/admin/admin-login/", "/admin/admin-login/", "/admin-login/",
        "/login/", "/modelsearch/login/", "/moderator/", "/moderator/login/", "/moderator/admin/",
        "/account/", "/controlpanel/", "/admincontrol/",
        "/rcjakar/admin/login/", "/webadmin/", "/webadmin/index/", "/webadmin/admin/",
        "/webadmin/login/", "/admin/admin_login/", "/admin_login/",
        "/panel-administration/login/", "/admin/cp/", "/cp/",
        "/administrator/account/", "/administrator/",
        "/access/", "/login/", "/modelsearch/login/",
        "/moderator/", "/moderator/login/", "/administrator/login/",
        "/moderator/admin/", "/controlpanel/", "/user/",
        "/admincontrol/", "/adminpanel/", "/webadmin/",
        "/webadmin/index/", "/webadmin/admin/",
        "/webadmin/login/", "/admin/admin_login/", "/admin_login/",
        "/panel-administration/login/", "/adminLogin/", "/admin/adminLogin/",
        "/home/", "/adminarea/index/", "/adminarea/admin/",
        "/adminarea/login/", "/panel-administration/index/",
        "/panel-administration/admin/", "/modelsearch/index/", "/modelsearch/admin/",
        "/admincontrol/login/", "/adm/admloginuser/", "/admloginuser/",
        "/admin2/", "/admin2/login/", "/admin2/index/", "/usuarios/login/",
        "/adm/index/", "/adm/", "/affiliate/", "/adm_auth/", "/memberadmin/",
        "/administratorlogin/", "/admin/account.js/", "/admin/index.js/",
        "/admin/login.js/", "/admin/admin.js/",
        "/admin_area/admin.js/", "/admin_area/login.js/", "/siteadmin/login.js/",
        "/siteadmin/index.js/", "/admin_area/index.js/", "/bb-admin/index.js/",
        "/bb-admin/login.js/", "/bb-admin/admin.js/", "/admin/home.js/",
        "/admin/controlpanel.js/", "/admin.js/", "/admin/cp.js/", "/cp.js/",
        "/administrator/index.js/", "/administrator/login.js/", "/nsw/admin/login.js/",
        "/webadmin/login.js/", "/admin/admin_login.js/", "/admin_login.js/",
        "/administrator/account.js/", "/administrator.js/",
        "/pages/admin/admin-login.js/", "/admin/admin-login.js/", "/admin-login.js/",
        "/login.js/", "/modelsearch/login.js/", "/moderator.js/",
        "/moderator/login.js/", "/moderator/admin.js/", "/account.js/",
        "/controlpanel.js/", "/admincontrol.js/",
        "/rcjakar/admin/login.js/", "/webadmin.js/", "/webadmin/index.js/", "/access.js/",
        "/webadmin/admin.js/", "/adminpanel.js/", "/user.js/",
        "/panel-administration/login.js/", "/wp-login.js/", "/adminLogin.js/",
        "/admin/adminLogin.js/", "/home.js/", "/adminarea/index.js/",
        "/adminarea/admin.js/", "/adminarea/login.js/", "/panel-administration/index.js/",
        "/panel-administration/admin.js/", "/modelsearch/index.js/", "/modelsearch/admin.js/",
        "/admincontrol/login.js/", "/adm/admloginuser.js/", "/admloginuser.js/",
        "/admin2.js/", "/admin2/login.js/", "/admin2/index.js/", "/usuarios/login.js/",
        "/adm/index.js/", "/adm.js/", "/affiliate.js/", "/adm_auth.js/", "/memberadmin.js/",
        "/admin_panel/", "/admin_panel.html/", "/adm_cp/",

        # Portuguese
        "/administrar/", "/painel/", "/paineladmin/", "/admgeral/", "/adminpainel/", "/administrador/",
        "/gerente/", "/painelgerente/", "/sistemaadmin/", "/adminpainelgeral/",
        "/paineladministrativo/", "/adminpaineladm/", "/paineldecontrole/", "/adminpaineldecontrole/",
        "/paineldoadministrador/", "/paineldogerente/", "/adminpaineldosistema/", "/adminpaineldeadministracao/",
        "/administracao/", "/paineladministracao/", "/adminpainelgeral/", "/paineldeadministracao/",
        "/adminpainelgeraldeadministracao/", "/paineldegerenciamento/", "/paineldecontroledeadministracao/",
        "/paineldosistemaadministrativo/", "/representantes.php/"
    ]

    for admin in payload:
        try:
            full_url = url + admin
            response = requests.get(full_url)
            status_code = response.status_code

            if status_code == 200:
                print(full_url + Fore.GREEN + "--> Found!")
            elif status_code == 403:
                print(full_url + "--> Forbidden")
            elif status_code == 404:
                print(full_url + Fore.RED + "--> Not Found :(")
            elif status_code == 302:
                print(full_url + "--> Redirecting -_-")
            else:
                print(Fore.BLUE + full_url + Fore.RESET + f"--> {status_code}")

        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Error for {admin}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, help='URL To Be Attacked!')
    args = parser.parse_args()

    if args.url:
        search_panel(args.url)
    else:
        print(Fore.RED + "Please provide a target URL using the -u or --url option.")
