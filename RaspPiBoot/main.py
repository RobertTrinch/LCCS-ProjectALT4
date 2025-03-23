# Please note: Making the device generate the GUID itself rather than the server is generally poor practice and can lead some risks.
import requests
import uuid
import datetime
import time
#from gpiozero import DistanceSensor

# Ultrasonic Sensors and their pins (guide: https://projects.raspberrypi.org/en/projects/physical-computing/12)
# Sensor 1 should be closest to the door (entrance would be triggered in the order of 1 then 2)
SENSOR1_echoPin = 1
SENSOR1_triggerPin = 2
SENSOR1_isTriggered = False
SENSOR2_echoPin = 3
SENSOR2_triggerPin = 4
SENSOR2_isTriggered = False
#sensor1 = DistanceSensor(echo=SENSOR1_echoPin, trigger=SENSOR1_triggerPin, max_distance=3, threshold_distance=0.5)
#sensor2 = DistanceSensor(echo=SENSOR2_echoPin, trigger=SENSOR2_triggerPin, max_distance=3, threshold_distance=0.5)

# API / Identifiers / API Calls
apiUrl = "API_URL_HERE"
deviceIdFile = "device-id.txt"
setDeviceId = ""

# API - Create a movement log
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

# API - Create a Device / Add a device to the database
def CreateDevice(guid):
    global setDeviceId
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
        print("Device Created with ID: " + str(guid))
        setDeviceId = str(guid)
    else:
        print("API returned Status Code other than 201: " + str(response.status_code))
        raise Exception("API Error when creating a Device")

# API - Get a device info by GUID
def GetDevice(guid):
    url = apiUrl + "Devices/" + guid
    data = requests.get(url)
    if(data.status_code == 200):
        return data.json()
    else:
        return 0
    
# Sensor Triggered Events
def OnSensor1Triggered():
    global SENSOR1_isTriggered, SENSOR2_isTriggered
    SENSOR1_isTriggered = True
    time.sleep(0.3) # Delay to allow the user to move to the next sensor
    if(SENSOR2_isTriggered == False):
        CreateMovement(True)
        print("Movement Detected: Entry")
    SENSOR1_isTriggered = False # Reset values
    SENSOR2_isTriggered = False

def OnSensor2Triggered():
    global SENSOR1_isTriggered, SENSOR2_isTriggered
    SENSOR2_isTriggered = True
    time.sleep(0.3) # Delay to allow the user to move to the next sensor
    if(SENSOR1_isTriggered == False):
        CreateMovement(False)
        print("Movement Detected: Exit")
    SENSOR1_isTriggered = False # Reset values
    SENSOR2_isTriggered = False

# Device Registration/Verification
print("Checking device ID..")
file = open(deviceIdFile, "r")
setDeviceId = file.read()
file.close()

if(setDeviceId == ""):
    print("No device ID found, creating a new device..")
    CreateDevice(str(uuid.uuid4()))
else:
    if(GetDevice(setDeviceId) == 0):
        print("Device ID stored is invalid, creating a new device..")
        CreateDevice(str(uuid.uuid4()))
    else:
        print("Device ID check successful: " + setDeviceId)

print("Beginning monitoring (Device ID: " + setDeviceId + ")")

#sensor1.when_in_range = OnSensor1Triggered
#sensor2.when_in_range = OnSensor2Triggered

while True:
    time.sleep(0)