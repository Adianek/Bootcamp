import requests
import json

localization = sys.argv[1]

def get_location_id(localization):

resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={localization}")
location_id = resp.json()[0]['woeid']

print(location_id)

# pobieram pogodę dla lokalizacji

resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}")
weather = resp.json()['consolidated_weather'][0]

print(weather)

# drukuję informację o pogodzie

print(f"Pogoda w lokalizacji: {localization}")
print("temperatura: ", weather['the_temp'])
print("ciśnienie powietrza", )
