"""Komunikacja_Klient_Serwer \
"""
import sys
from django.conf.urls import url
from django.contrib import admin

from Komunikacja_Klient_Serwer import CommSocket

urlpatterns = [url(r'^admin/', admin.site.urls), ]

comm = CommSocket.CommSocket()

comm.connect('127.0.0.1', 8050)

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

sys.exit(0)
