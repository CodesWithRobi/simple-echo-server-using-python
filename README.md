# Echoserver
Echo server and client using python socket

# AIM:

To develop an echo server and client using python socket

## DESIGN STEPS:

### Step 1:

Design of echo server and client using python socket

### Step 2:

Implementation using Python code

### Step 3:

Testing the server and client 

## PROGRAM:

```

Server code

# echo-server.py

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


Client Code:
# echo-client.py

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

```

## OUTPUT:

Run server first
➜  simple-echo-server-using-python git:(main) python3 echo-server.py 
Connected by ('127.0.0.1', 42596)
Note: Connected message will appear only after running echo-client.py 

In another terminal run client
➜  simple-echo-server-using-python git:(main) python3 echo-client.py 
Enter a message to send : Hello, world!
Received Hello, world!

## RESULT:
The program is executed successfully
