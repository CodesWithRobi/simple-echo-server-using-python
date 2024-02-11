import socket

HOST = 'localhost'
PORT = 9999
SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.connect((HOST, PORT))
   msg = input("Enter a message to send : ")
   s.sendall(bytes(msg, 'utf-8'))
   data = s.recv(SIZE) #Receiving from the server

print(f"Received {data.decode()}")

