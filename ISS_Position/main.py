import requests
from datetime import datetime
import time
import smtplib

my_email = "akvilary@yahoo.com"
password = "SUPERSECRET"
subject = "Look at the sky to see ISS!"
message = None

my_latitude = 55.030521
my_longitude = 82.977483

iss_latitude = None
iss_longitude = None

data = None
sunrise_date = None


def local_time(time, utc):
    global sunrise_date

    if (time + utc) > 24:
        sunrise_date[2] = int(sunrise_date[2]) + 1
        new_day_our = (time + utc) % 24
        return new_day_our
    else:
        day_hour = time + utc
        return day_hour


def get_data(url_address, r_params = None):
    global data

    server_response = requests.get(url=url_address, params=r_params)
    server_response.raise_for_status()
    data = server_response.json()


def is_iss_overhead():
    global iss_latitude
    global iss_longitude

    get_data('http://api.open-notify.org/iss-now.json')
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if my_latitude - 5 <= iss_latitude <= my_latitude + 5 \
        and my_longitude - 5 <= iss_longitude <= my_longitude + 5:
        return True

def is_nighttime():

    parameters = {
        'lat': my_latitude,
        'lng': my_longitude,
        'formatted': 0,
    }

    get_data('https://api.sunrise-sunset.org/json', parameters)


    sunrise = data['results']['sunrise']
    sunrise_date = sunrise.split('T')[0].split('-')
    sunrise_time = sunrise.split('T')[1].split('+')[0].split(':')
    sunrise_hour = local_time(int(sunrise_time[0]), 7)
    sunrise_minute = int(sunrise_time[1])

    sunset = data['results']['sunset']
    sunset_date = sunset.split('T')[0].split('-')
    sunset_time = sunset.split('T')[1].split('+')[0].split(':')
    sunset_hour = local_time(int(sunset_time[0]), 7)
    sunset_minute = int(sunset_time[1])

    time_now = datetime.now()

    if sunset_hour <= time_now.hour <= sunrise_hour \
            and sunset_minute <= time_now.minute <= sunrise_minute:
        return True


def send_message():
    message = f"Look at the sky ASAP!" \
              f"You are located in:" \
              f"    latitude {my_latitude}" \
              f"    longitude {my_longitude}" \
              f"The ISS is near and located in:" \
              f"    latitude {iss_latitude}" \
              f"    longitude {iss_longitude}"

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="a.mathgame.s@gmail.com",
            msg=f"Subject:{subject}\n\n{message}")


while True:
    if is_iss_overhead() and is_nighttime():
        send_message()
    time.sleep(60)