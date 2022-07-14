import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "YOUR API KEY from OPENWEATHERMAP"
account_sid = "YOUR ACCOUNT SID from TWILIO"
auth_token = "YOUR AUTHENTICATION TOKEN from TWILIO"


weather_params = {
    "lat": -12.9711,
    "lon": -38.5108,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_id = hour_data["weather"][0]["id"]
    if int(condition_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Today it´s going to rain!",
        from_="YOUR TWILIO PHONE NUMBER",
        to="YOUR PERSONAL NUMBER USED TO REGISTER IN TWILIO"
    )

    print(message.status)
