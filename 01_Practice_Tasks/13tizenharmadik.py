import requests
from bs4 import BeautifulSoup

print("1. Weboldal letöltése...")
valasz = requests.get("https://example.com")

leves = BeautifulSoup(valasz.text, "html.parser")

print("2. Adatok kibányászása...")


focim = leves.find("h1").text
bekezdes = leves.find("p").text

print("\n--- A BÁNYÁSZAT EREDMÉNYE ---")
print("A weboldal főcíme:", focim)
print("A bekezdés szövege:", bekezdes)