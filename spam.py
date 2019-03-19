import random
from fbchat import Client
from fbchat.models import *


def menu():
    email = input("Email: ")
    passw = input("Password: ")
    client = Client(email, passw)
    usertospam = input("Users Name: ")
    users = client.searchForUsers(usertospam)
    user = users[0]
    print ("1. Ascii Spammer\n2. Custom Message Spam")
    choice = input("Choice: ")
    try:
        if int(choice) == 1:
            asciispam(client,user)
        elif int(choice) == 2:
            customspam(client,user)
        else:
            menu()
    except:
        menu()


def asciispam(client,user):
    while True:
        try:
            asc = ""
            for x in range(1999):
                num = random.randrange(15000)
                asc = asc + chr(num)
            client.send(Message(text=asc), thread_id=user.uid, thread_type=ThreadType.USER)
        except Exception as e:
            print (e)

def customspam(client,user):
    custom = input("Text to spam: ")
    while True:
        try:
            client.send(Message(text=custom), thread_id=user.uid, thread_type=ThreadType.USER)
        except Exception as e:
            print (e)

menu()
