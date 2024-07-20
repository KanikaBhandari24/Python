import smtplib

email="kanikabhandari2417@gmail.com"
Pass="password dalo"

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email, password=Pass)  
connection.sendmail(from_addr=email, to_addrs=email, msg="Hello this is an email sent to you while learning and testing PYTHON.")
connection.close()
