import socket
import threading

server_socket = socket.socket()

print("Socket Created")

server_socket.bind(("127.0.0.1",6100))

server_socket.listen(2)

print("Waiting for Connections")

def handle_one_client(client_socket,address):

    print(f"Connected with {address}")

    try:
        while True:

            data = client_socket.recv(1024) # Receive data from Client

            if not data:
                break

            print(f"Data Received from {address} : {data.decode()}")

            #client_socket.send(f"server received your message : {data.decode()}")

    except Exception as e:
        print(f"Error handling client {address} : {e}")

    finally:
        client_socket.close()
        print(f"connection with {address} closed.")


while True:

    client_socket , address = server_socket.accept()  # Accept New Connections

    # Create a new thread to handle a new incoming client

    client_handler = threading.Thread(target = handle_one_client , args = (client_socket,address))

    client_handler.start()

