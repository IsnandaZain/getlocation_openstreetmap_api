import requests

lat = input("input your coordinates (lat) : ")
lng = input("input your coordinates (long) : ")

try:
    result = requests.get("https://nominatim.openstreetmap.org/reverse?format=geojson&lat={}&lon={}&zoom=18&addressdetails=1".format(str(lat), str(lng))).json()
except:
    raise ("Gagal mendapatkan info lokasi")

# get all information in address
info_address = result["features"][0]["properties"]["address"]

# check if address have state
if "state" in info_address:
    if "city" in info_address:
        city = info_address["city"]

    elif "county" in info_address:
        city = info_address["county"]

    elif "town" in info_address:
        city = info_address["town"]

    elif "village" in info_address:
        city = info_address["village"]

    else:
        city = "Unknown"

    state = info_address["state"]
else:
    if "city" in info_address:
        state = info_address["city"]
        if "county" in info_address:
            city = info_address["county"]
        else:
            city = "Unknown"
    else:
        state = "Unknown"
        city = "Unknown"

location = [city, state]

print("hasil lokasi - Kota : %s" % location[0])
print("hasil lokasi - Provinsi : %s" % location[1])