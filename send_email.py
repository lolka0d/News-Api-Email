import smtplib, ssl
import configparser

config = configparser.ConfigParser()

config.read("config.ini")

host = "smtp.gmail.com"
port = 465

login = config["EMAIL"]["LOGIN"]
password = config["EMAIL"]["PASSWORD"]


def send_email(message: str) -> tuple:
    try:
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(login, password)
            server.sendmail(login, login, message)

        return True, 0
    except Exception as e:
        return False, e

