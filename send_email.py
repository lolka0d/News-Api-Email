import smtplib, ssl
import os

host = "smtp.gmail.com"
port = 465

username = "contactmedata72@gmail.com"
email_pass = os.getenv("EMAIL_PASS")


def send_email(message: str) -> tuple:
    try:
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(username, email_pass)
            server.sendmail(username, username, message)

        return True, 0
    except Exception as e:
        return False, e

