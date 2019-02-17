import requests
import json

resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")
kursy = resp.json()[0]['rates']
print(kursy)

print("Dysponuję walutami: ")
for k in kursy:
    print(k)
waluta = input("Podaj kod waluty, którą chcesz kupić: ")
za_ile = float(input("Za ile PLN chcesz kupić? "))
for k in kursy:
    if k['code'] == waluta:
        print(f"Za {za_ile} PLN możesz kupić {za_ile/k['mid']:.2f} {waluta}") # do dwóch miejsc po przecinku
# resp.content
# resp.json()
# print(resp)
#
# with open("kursy.json", "wb") as f:
#     json.dump(resp, f)
#
#
# for i in resp:
#     if i['currency'] == 'euro':
#         print(i)
#
