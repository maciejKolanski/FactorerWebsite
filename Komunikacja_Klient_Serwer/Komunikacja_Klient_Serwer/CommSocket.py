import socket


class CommSocket:
    def __init__(self):
        self.reply = ""
        self.packet_size = 0
        try:
            self.socket_desc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('Socket created')
        except socket.error as msg:
            print('Failed to create socket. Error code: ' + str(msg[0]) + ' Error code: ' + str(msg[1]))

    def __del__(self):
        self.socket_desc.close()
        print('Socket closed')

    def connect(self, remote_ip, port):

        try:
            self.socket_desc.connect((remote_ip, port))
            print('Socket Connected to ip ' + remote_ip)
        except socket.error:
            print('Failed to connect')

    def disconnect(self):
        self.socket_desc.close()
        print('Socket closed')

    def send(self, message):

        try:
            self.socket_desc.sendall((len(message)).to_bytes(4, byteorder='big'))
            print('Message send successfully')
        except socket.error:
            print('Send failed')
            return 1

        try:
            self.reply = self.socket_desc.recv(8)
            print('Command received')
        except socket.error:
            print('Command receive failed')
            return 1

        self.reply = self.reply.decode(encoding='utf-8')
        self.reply = self.reply[:-1]

        if self.reply == 'ACCEPTD':
            try:
                self.socket_desc.sendall(bytes(message, 'utf-8'))
                print('Message send successfully')
            except socket.error:
                print('Send failed')
                return 1
        else:
            print('Unknown command')
            return 1

        return 0

    def receive(self):
        try:
            self.packet_size = self.socket_desc.recv(4)
            self.packet_size = int.from_bytes(self.packet_size, byteorder='big')

            if self.packet_size <= 0:
                print('Connection closed')
                self.socket_desc.close()
                return 1

            print('Size receive success: ', self.packet_size)
        except socket.error:
            print('Size receive failed')
            return 1

        try:
            self.socket_desc.sendall(bytes('ACCEPTD' + '\0', 'utf-8'))
            print('Command send successfully')
        except socket.error:
            print('Command send failed')
            return 1

        try:
            self.reply = self.socket_desc.recv(self.packet_size)
            print('Packet receive success')
        except socket.error:
            print('Packet receive failed')
            return 1

        self.reply = self.reply.decode(encoding='utf-8')

        return 0
