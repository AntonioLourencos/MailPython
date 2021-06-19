import json
import smtplib
with open("./src/config/stmp.json") as f:
    config = json.load(f)
    host: str = config["host"]
    port: int = config["port"]
    email: str = config["email"]
    password: str = config["password"]


class EmailModuler:
    def send(emailUser: str):
        msg = '''
            My first email sent with python
        '''
        server = smtplib.SMTP(host, port)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, emailUser, msg)
        server.quit()
        return "sucess"
