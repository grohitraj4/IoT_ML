Code for conf.py
"""Configurations for telegram_alert.py"""
bolt_api_key = "XXXX"               # This is your Bolt Cloud API Key
device_id = "XXXX"                  # This is the device ID and will be similar to BOLTXXXX where XXXX is some numbers
telegram_chat_id = "@XXXX"          # This is the channel ID of the created Telegram channel. Paste after @
telegram_bot_id = "botXXXX"         # This is the bot ID of the created Telegram Bot. Paste after bot
threshold = 250                     # Threshold beyond which the alert should be sent

Code for telegram_alert.py
NOTE - To exit from a While loop, press CTRL + C on your keyboard.

import requests                 # for making HTTP requests
import json                     # library for handling JSON data
import time                     # module for sleep operation

from boltiot import Bolt        # importing Bolt from boltiot module
import conf                     # config file

mybolt = Bolt(conf.bolt_api_key, conf.device_id)

def get_sensor_value_from_pin(pin):
    """Returns the sensor value. Returns -999 if request fails"""
    try:
        response = mybolt.analogRead(pin)
        data = json.loads(response)
        if data["success"] != 1:
            print("Request not successfull")
            print("This is the response->", data)
            return -999
        sensor_value = int(data["value"])
        return sensor_value
    except Exception as e:
        print("Something went wrong when returning the sensor value")
        print(e)
        return -999


def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram URL")
        print(url)
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False


while True:
    # Step 1
    sensor_value = get_sensor_value_from_pin("A0")    
    print("The current sensor value is:", sensor_value)
    
    # Step 2
    if sensor_value == -999:
        print("Request was unsuccessfull. Skipping.")
        time.sleep(10)
        continue
    
    # Step 3
    if sensor_value >= conf.threshold:
        print("Sensor value has exceeded threshold")
        message = "Alert! Sensor value has exceeded " + str(conf.threshold) + \
                  ". The current value is " + str(sensor_value)
        telegram_status = send_telegram_message(message)
        print("This is the Telegram status:", telegram_status)

    # Step 4
    time.sleep(10)