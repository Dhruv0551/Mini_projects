import requests
from datetime import datetime

fitness_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_url = "https://api.sheety.co/YOUR_PROJECT_TOKEN/YOUR_PROJECT_NAME/YOUR_SHEET_NAME"

headers = {
    "x-app-id": "YOUR_APP_ID",
    "x-app-key": "YOUR_API_KEY"
}

user_input = input("What did you do today? ")

user_params = {
    "query": user_input,
    "gender": "YOUR_GENDER",
    "weight_kg": YOUR_WEIGHT_KG,
    "height_cm": YOUR_HEIGHT_CM,
    "age": YOUR_AGE
}

response = requests.post(url=fitness_endpoint, json=user_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_params = {
        "sheet1": {
            "Date": today_date,
            "Time": now_time,
            "Exercise": exercise["name"].title(),
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_url, json=sheet_params)
    print("Response from Sheety:")
    print(sheet_response.status_code)
    print(sheet_response.text)
