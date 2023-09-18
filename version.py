import requests

print(requests.__version__)

r = requests.get("https://google.com")

r = requests.get("https://raw.githubusercontent.com/qasim-tech/Cmput404-Lab1/master/version.py")

print(r.text)
