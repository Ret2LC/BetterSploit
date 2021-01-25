import requests
import sys

r = requests.get("http://shell-storm.org/api/?s="+sys.argv[1])
print(r.text)
