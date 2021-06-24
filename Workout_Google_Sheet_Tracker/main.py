import os
import requests
import pytz
from datetime import datetime

DATE = datetime.now(pytz.timezone('Asia/Novosibirsk'))
TODAY = DATE.strftime("%x")
TIME = DATE.strftime("%X")

API_ID = os.environ['API_ID']
API_KEY = os.environ['API_KEY']

EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_ENDPOINT = 'https://api.sheety.co/7427e165a7ddef6ac6de2ca00e62e542/workoutTracking/workouts'

SHEETY_AUTH_KEY = os.environ['Authorization']

GENDER = 'male'
WEIGHT_KG = 78
HEIGHT_CM = 180
AGE = 28

headerset = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0',
}

query = input("Write your phisical exercise and quantity of km or times: \n")

personset = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response1 = requests.post(url=EXERCISE_ENDPOINT, json=personset, headers=headerset)
EXER_DATA = response1.json()


sheety_header = {
    'Authorization': SHEETY_AUTH_KEY,
}

for exercise in EXER_DATA["exercises"]:
    sheet_input = {
        'workout': {
            'date': TODAY,
            'time': TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response2 = requests.post(url=SHEETY_ENDPOINT, json=sheet_input, headers=sheety_header)

    print(response2.text)