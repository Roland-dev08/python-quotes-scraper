import requests
from bs4 import BeautifulSoup

print("Weboldal letöltése...")
valasz = requests.get("https://example.com")
leves = BeautifulSoup(valasz.text, "html.parser")

bekezdesek = leves.find_all("p")

print("\n--- Az összes bekezdés kibányászása ---")

for bekezdes in bekezdesek:
    print("Bekezdés szövege:", bekezdes.text)