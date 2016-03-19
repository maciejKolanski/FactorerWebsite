"""Komunikacja_Klient_Serwer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import socket
import sys

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

try:
    socket_desc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + 'Error code: ' + str(msg[1]))
    sys.exit()

print('Socket created')

host = 'localhost'

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('Ip address of ' + host + ' is ' + remote_ip)

socket_desc.connect((remote_ip, 8888))

print('Socket Connected to ' + host + ' on ip ' + remote_ip)
ack = 'ACCEPTD'

while True:

    message = input() + '\0'
    if message == 'exit\0':
        sys.exit()

    # print((len(message)).to_bytes(4, byteorder='big'))

    try:
        socket_desc.sendall((len(message)).to_bytes(4, byteorder='big'))
        print('Message send successfully')
    except socket.error:
        print('Send failed')
        sys.exit()

    try:
        reply = socket_desc.recv(8)
        print('Command received')
    except socket.error:
        print('Command receive failed')
        sys.exit()

    print(reply)

    reply = reply.decode(encoding='utf-8')

    reply = reply[:-1]

    if reply == ack:
        try:
            socket_desc.sendall(bytes(message, 'utf-8'))
            print('Message send successfully')
        except socket.error:
            print('Send failed')
            sys.exit()
    else:
        print('Not equal')
        sys.exit()

    # Odpowiedz z serwera
    try:
        packet_size = socket_desc.recv(4)
        packet_size = int.from_bytes(packet_size, byteorder='big')
        print('Size receive success: ', packet_size)
    except socket.error:
        print('Size receive failed')
        sys.exit()

    try:
        socket_desc.sendall(bytes(ack + '\0', 'utf-8'))
        print('Command send successfully')
    except socket.error:
        print('Command send failed')
        sys.exit()

    try:
        reply = socket_desc.recv(packet_size)
        print('Packet receive success')
    except socket.error:
        print('Packet receive failed')
        sys.exit()

    reply = reply.decode(encoding='utf-8')

    print(reply)

sys.exit(0)
