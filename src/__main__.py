from os import system
from time import sleep
from module.mail import EmailModuler


def sendQuestion():
    system("clear")
    sendMail = input("Do you want to send a email? (Y/N): ")
    sendMail = sendMail.lower()
    if(not sendMail):
        print("Your answer no have value...")
        sleep(3)
        sendQuestion()

    if(not (sendMail == "y" or sendMail == "n")):
        print("your answer should be Y or N")
        sleep(3)
        sendQuestion()

    if(sendMail == "n"):
        print("Close application")
        return

    replyQuestions()


def replyQuestions():
    email = input("what is your email? ")

    if(not email):
        print("Your answer no have value...")
        sleep(3)
        sendQuestion()

    if(("@" in email) == False):
        print("You have not sent a valid e-mail.")
        sleep(3)
        sendQuestion()

    res = EmailModuler.send(emailUser=email)
    return res


sendQuestion()
