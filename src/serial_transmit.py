import datetime #Allows returning the date
#from pyserial import moisture_value
import serial #from pyserial package

# Importing the necessary mongo stuff
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jmbradecamp:Bbn028YcSIGBSrSI@tribehackix.j9oe55e.mongodb.net/?retryWrites=true&w=majority&appName=TribeHackIX"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.soil_data
collection = db.soil_collection
moistureValues = db.moistureValues

# copy the variable from the pyserial file to this file
#moistureValue = moisture_value

def addToDatabase(moistureValue):
    moistureValues.insert_one({"Value: ": moistureValue, "date": datetime.datetime.now(tz=datetime.timezone.utc)})

 
addToDatabase(650)  # Test number on this one, replace the 650 with the actual moisture number

#modify the usb name based on the computer used, PC uses COM
ser = serial.Serial('/dev/cu.usbmodem1412401', 9600)

while True:

    print(ser.readline())

    # reads the characters in the string corresponding to the integer moisture value
    current_value_byte_string = ser.readline()[16:]

    # test to see if the integer is correct
    print(current_value_byte_string)

    # convert the byte string to a string
    current_value_string_full = str(current_value_byte_string, encoding='utf-8')

    # test to see if the string is correctly encoded
    print(current_value_string_full)

    # convert the string to an integer for the final value
    moistureValue = int(current_value_string_full)

    # test if integer value is the same
    print(moistureValue)

    addToDatabase(moistureValue)
