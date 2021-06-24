##################### Extra Hard Starting Project ######################
#Modules
import smtplib
import datetime as dt
import pandas
import random

#Set variables
my_email = "akvilary@yahoo.com"
password = "SUPERSECRET"
subject = None
message = None

#Get today's date
now = dt.datetime.now()
date = (now.day, now.month)

#Read database of persons
db_birthdays = pandas.read_csv("birthdays.csv")

#Get all persons with birthday in current month
persons_in_month = db_birthdays[db_birthdays.month == date[1]]

#Get all persons with today's birthday
persons_today = persons_in_month[persons_in_month.day == date[0]]

#Get number of persons to congratulate
number_of_persons = len(persons_today.name)

#If there is any person to congratulate than do it
if number_of_persons > 0:

    #Get list of names
    names = persons_today.name.head()

    #Congratulate each of persons
    for xname in names:
        #Choose template
        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        letter_template = random.choice(letters)

        #Read letter template
        with open(f"./letter_templates/{letter_template}", 'r') as letterfile:
            letter = letterfile.read()

        #Replace name
        message = letter.replace("[NAME]", xname)

        #Get email_address
        to_email = persons_today.email[persons_today.name == xname]

        #Send email
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:{xname}, happy Birthday!\n\n{message}")








