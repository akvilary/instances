import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.my_email = "akvilary@yahoo.com"
        self.password = "mmzvgzcpojuuopya"
        self.to_email = "a.mathgame.s@gmail.com"
        self.subject = "Lowest prices for flights"

    def send_me_email(self, data):
        message = None

        for text in data:
            message += text

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=self.to_email,
                msg=f"Subject:{self.subject}\n\n{message}")