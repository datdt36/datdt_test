import smtplib
sender="sender@gmail.com"
receiver="receiver@gmail.com"
password="your_password"
subject="python test mail"
body="Toi test mail"

message= f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

count=0
for i in range(4):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(sender,password)
    print("Logged in...")

    server.sendmail(sender,receiver,message)
    print("Email has been sent...!")

