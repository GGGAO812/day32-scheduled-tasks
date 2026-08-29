import os
import smtplib
import datetime as dt
import pandas
import random


os.environ.get("MY_EMAIL")
os.environ.get("MY_PASSWORD")

data = pandas.read_csv("birthdays.csv")
dd = data.to_dict(orient="records")

def send_email(to,name):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        letter_use = f"./letter_templates/letter_{str(random.randint(1, 3))}.txt"
        with open(letter_use, "r") as f:
            content_send = f.read()
        send = content_send.replace("[NAME]", name)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=to,msg=f"Subject:Birthday!\n\n{send}")

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day


for _ in dd:
    if today_month == _["month"] and today_day == _["day"]:
        send_email(to = _["email"],name = _["name"])