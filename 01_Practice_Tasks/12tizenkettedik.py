import requests

print("Kapcsolódás az internethez...")

valasz = requests.get("https://example.com")

print("\n--- A WEBOLDAL IGAZI FORRÁSKÓDJA (HTML) ---")
print(valasz.text)