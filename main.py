import requests
import keys
import os
from twilio.rest import Client
api_key = keys.api_key
account_sid = keys.account_sid
auth_token = keys.auth_token

parameters = {
    "lat" : 25.374756,
    "lon" : 86.473526,
    "appid" : api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for i in range(0, 12):
    weather_id = weather_data['hourly'][i]['weather'][0]['id']
    if weather_id<700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an ☂️umbrella.",
        from_='+1 8563475458',
        to=f'+91 {keys.ph_no}' #Phone number on which we want to get message.
    )

    print(message.status)


