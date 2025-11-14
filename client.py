import socket

client_socket = socket.socket()

client_socket.connect(("127.0.0.1",6100))

while True:

    message = input("Let's Talk : ")

    client_socket.send(message.encode())

    if message.lower() == "bye":
        break

#message = client_socket.recv(1024).decode()

#print(message)
