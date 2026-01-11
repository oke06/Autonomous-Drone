import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("command".encode("utf-8"), ("192.168.10.1", 8889))
time.sleep(3)
client.sendto("streamon".encode("utf-8"), ("192.168.10.1", 8889))

while True:
    commandToSend = input("Send a command")

