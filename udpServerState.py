import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind("0.0.0.0", 8890)

while True:
    message, address = server.recvfrom(1024)
    print(message.decode("utf-8"))