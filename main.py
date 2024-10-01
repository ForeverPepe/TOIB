import hashlib
import pyhibp
from pyhibp import pwnedpasswords as pw
import requests


def leakcheck():
    with open('userlist.txt', 'r') as file:
        for line in file:
            a = line.split(',')
            name = a[0]
            password = a[1]
            pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
            resp = pw.is_password_breached(password=password)
            if resp:
                print("Пароль пользователя ",name," раскрыт")
            else:
                print("Пароль пользователя ", name, " не раскрыт")