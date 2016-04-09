"""Komunikacja_Klient_Serwer \
"""
import sys
from django.conf.urls import url
from django.contrib import admin

from Komunikacja_Klient_Serwer import CommSocket

urlpatterns = [url(r'^admin/', admin.site.urls), ]

comm = CommSocket.CommSocket()

comm.connect('127.0.0.1', 8060)

while True:

    message = input() + '\0'

    if message == 'exit\0':
        comm.disconnect()
        break

    if comm.send(message):
        break

    if comm.receive():
        break

    print(comm.reply)
    print(len(comm.reply))
    if comm.reply == 'IN_RES':

        message = 'START\0'
        if comm.send(message):
            break

        result = []

        while True:

            if comm.receive():
                break

            if comm.reply == 'RES_END':
                break
            else:
                result.append(comm.reply)

            message = 'NEXT\0'

            if comm.send(message):
                break

        for i in range(0, len(result)-1, 2):
            print(result[i], "*", result[i + 1])


sys.exit(0)
