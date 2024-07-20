import smtplib
import random
import datetime as dt

email="email dalo"
pass1="password dalo"

now=dt.datetime.now()
day1=now.weekday()
if day1 == 5: #5 is the weekday number the day i am making this project is  saturday which means 5 bcs list starts from 0 index
    with open("Quotes on your Email Project/quotes.txt") as file:
        all=file.readlines()
        quote=random.choice(all)
    print(quote)

    #setting the connection to send mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, pass1)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Monday Motivation\n\n{quote}")
