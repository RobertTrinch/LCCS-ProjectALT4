# Please note: Making the device generate the GUID itself rather than the server is generally poor practice and can lead some risks.

import requests
import uuid
import datetime

apiUrl = "API_URL_HERE"
deviceIdFile = "device-id.txt"
setDeviceId = ""

def CreateMovement(entry: bool):
    url = apiUrl + "Movements"
    data = {
        "movementGuid": str(uuid.uuid4()),
        "device": setDeviceId,
        "movementTime": datetime.datetime.now().replace(" ", "T") + "Z",
        "entry": entry
    }
    response = requests.post(url, json=data)
    return response.status_code

def CreateDevice(guid):
    url = apiUrl + "Devices"
    data = {
        "deviceGuid": str(guid),
        "displayName": "New Device",
        "displayLocation": "New Device Location",
        "currentDeviceAmount": 0
    }
    response = requests.post(url, json=data)
    if(response.status_code == 201):
        file = open(deviceIdFile, "w")
        file.write(str(guid))
        file.close()
        print("Device Created with ID:" + str(guid))
        setDeviceId = str(guid)
    else:
        print("API returned something that wasnt a 201")

def GetDevice(guid):
    url = apiUrl + "Devices/" + guid
    data = requests.get(url)
    if(data.status_code == 200):
        return data.json()
    else:
        return 0

# -- Device Registration
# Open file to check if anything there

file = open(deviceIdFile, "r")

if(file.read() == ""):
    file.close()
    CreateDevice(str(uuid.uuid4()))
else:
    if(GetDevice(file.read()) == 0):
        CreateDevice(str(uuid.uuid4()))
    else:
        setDeviceId = file.read()

# Sensor Logic
