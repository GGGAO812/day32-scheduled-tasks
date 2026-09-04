import requests
import smtplib
import os
# from twilio.rest import Client


# SID = "SKc24242aa2625aea49027ed04f27ceaa4"
# CLIENT_SECRET = "SKc24242aa2625aea49027ed04f27ceaa4"

# SID = "ACbff6aa12280263803478b7758e8eee6d"
# CLIENT_SECRET =  "45945513f275f0a13810a906417297ee"
#
# account_sid = SID
# auth_token = CLIENT_SECRET
# client = Client(account_sid, auth_token)

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.environ.get("API_KEY")

# an_shan_lat_long = {"lat":41.1236,
#              "lon":122.99}

weather_parameter = {"lat":26.05,
             "lon":119.18,
             "cnt":4,
             "appid":os.environ.get("API_KEY")
             }

response = requests.get(OWM_Endpoint, params=weather_parameter)
# print(response.status_code)
# response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <700 :
        will_rain = True
if will_rain:
    with smtplib.SMTP('smtp.163.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject:ALTER!\n\nRemember bring an umberlla" )

    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It`s going to rain!Remember bring the Umbrella!",
    #     from_="+17372508034",
    #     to="",
    # )
    # print(message.status)
