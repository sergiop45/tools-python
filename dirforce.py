import requests
import sys

url = 'https://' + sys.argv[1]

diretorios_comuns = [    "admin",    "adm",    "administrator",    "backup",    "bin",
    "cgi-bin",    "css",    "data",    "docs",    "download",    "images",    "includes", 
       "js",    "lib",    "logs",    "media",    "public",    "scripts",    "src",    "static", 
          "test",    "tmp",    "uploads",    "web",    "webadmin",    "webmail",    "wp-admin", 
                "wp-content",    "wp-includes"]


print("Realizando busca de diretorios em {}".format(url))

for word in diretorios_comuns:
    url_final = "{}/{}".format(url, word)
    response = requests.get(url_final)
    code = response.status_code
    print(f"{url_final} -> codigo: {code}")
