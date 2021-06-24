import smtplib
import datetime as dt
import random

my_email = "akvilary@yahoo.com"
password = "SUPERSECRET"
subject = "Weekly quote"
message = None

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt", 'r') as file:
        quotes = file.readlines()
        message = random.choice(quotes)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="a.mathgame.s@gmail.com",
            msg=f"Subject:{subject}\n\n{message}")


# year = now.year
# month = now.month
# date_of_birth = dt.datetime(year=1993, month=1, day=31)
# print(date_of_birth)

