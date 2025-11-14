import socket

server_socket = socket.socket()

print("Socket Created")

server_socket.bind(("127.0.0.1",6100))

server_socket.listen(3)

print("Waiting for Connections")

client_socket , address = server_socket.accept()

while True:

    message = client_socket.recv(1024).decode()

    print("Connected with",address,message)

    #client_socket.close()

#client_socket.send(message.encode())


