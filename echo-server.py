import socket

HOST = 'localhost'
PORT = 9999
SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.bind((HOST, PORT)) 
   s.listen()
   conn, addr = s.accept()
   with conn:
       print(f"Connected by {addr}")
       while True:
           data = conn.recv(SIZE) #Receive the data from client
           if not data:
               break
           conn.sendall(data) #Send back the data to client
