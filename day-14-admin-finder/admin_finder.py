#!/usr/bin/python3


import requests


admin_paths_dic = [
    "/admin",
    "/admin/login",
    "/admin.php",
    "/admin.html",
    "/administrator",
    "/administrator/login",
    "/adminpanel",
    "/controlpanel",
    "/cpanel",
    "/backend",
    "/backend/login",
    "/dashboard",
    "/admin-area",
    "/admin_area",
    "/adm",
    "/wp-admin",         # WordPress
    "/wp-login.php",     # WordPress
    "/user/login",
    "/login",
    "/system",
    "/console",
    "/secure",
    "/manage",
    "/moderator",
    "/mod",
    "/siteadmin",
    "/admincp",
    "/memberadmin"
]

def admin_finder(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    for paths in admin_paths_dic:
        admin_url = f"{url}{paths}"
        try:
            r = requests.get(admin_url,timeout=2)
        except requests.RequestException as er:
            print(f"[+] ERROR >> {er}")
            exit()
        try:
            if r.status_code < 400:
                print(f"Status code >> [{r.status_code}] -- url >> {admin_url}")
        except requests.RequestException  as re:
            print(f"Error {re}")

if __name__ == "__main__":
    admin_finder(url='example.com')

