import requests

URL = "http://api.open-notify.org/astros.json"


astro= requests.get(URL).json()

print(astro["number"])

for astrodict in astro["people"]:
    print(f"astrodict['name']} is on the {each_astro.get('craft')}")
