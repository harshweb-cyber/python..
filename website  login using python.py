import requests
import webbrowser

session = requests.session()

r = session.get("https://gulms.galgotiasuniversity.org")

url = "https://gulms.galgotiasuniversity.org"
data = {"login": "admin", "password": "admin""}

file = open("file.html" , "wb")
file.write(r.content)
file.close()

webbrowser.open("file.html")
