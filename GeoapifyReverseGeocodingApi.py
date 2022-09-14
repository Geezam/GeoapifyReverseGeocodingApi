import requests, csv
from requests.structures import CaseInsensitiveDict

#API key of your project
geoapify = "PUT-YOUR-API-KEY-HERE"

#initialise records list and lat, lon float variables
records = []
lat = 0.0
lon = 0.0

#url parts to be put together specifying JSON format
#Geoapify allows 'json', 'xml', or 'geojson' (default)
link1 = "https://api.geoapify.com/v1/geocode/reverse?"
link2 = "format=json&apiKey="

#EXAMPLE CSV file with records of 5 airports across the Caribbean
#save each airport coordinate into a dictionary array within the records list
with open("caribbean_airports.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        record = {
        "lat": 0.0,
        "lon": 0.0}
        if line_count == 0:
            line_count += 1
        else:
            record["lat"] = float(row[0])
            record["lon"] = float(row[1])
            records.append(record)
            line_count += 1
        
#loop through and view each record
for cord in records:
    print(cord)
""" OUTPUT    
{'lat': 17.93644564240522, 'lon': -76.77887154784555}
{'lat': 18.576469251350392, 'lon': -72.29583239907271}
{'lat': 13.079748830120481, 'lon': -59.487715973535956}
{'lat': 12.007459857934851, 'lon': -61.78592481196946}
{'lat': 10.597751926559294, 'lon': -61.33846862517268}
"""

#create a url string that has all the parts geoapify needs
#array has five record [0] to [4]. Let's use the 1st one
lat = "lat=" + str(records[0]["lat"]) + "&"
lon = "lon=" + str(records[0]["lon"]) + "&"
url = link1 + lat + lon + link2 + geoapify

#access geoapify API with credentials
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
resp = requests.get(url, headers=headers)

#Choose data to be displayed from JSON output received
print(resp.json()["results"][0]["name"])
print(resp.json()["results"][0]["city"])
print(resp.json()["results"][0]["country"])

""" OUTPUT
Norman Manley International Airport
Kingston
Jamaica
"""

#remove the hash sign below to see full JSON output
#print(resp.json())