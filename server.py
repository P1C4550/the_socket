import socket, threading, time
from communicator import Communicator
#  smth_t  -  thread
#  smth_s  -  socket


class Server:
    def __init__(s, adress, port, socket_limit):
        s.adress = adress
        s.port = port
        s.socket_limit = socket_limit
        
        s.server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.server_s.bind((s.adress, s.port))
        s.server_s.listen(s.socket_limit)
        
        s.lock = threading.Lock()
        s.communicators = []
    
    def always_listen(s):
        client_socket, client_address = s.server_s.accept()
        client_ip, client_port  = client_socket.getsockname())
        s.communicators.append(Communicator(client_socket, s.lock, client_ip, client_port))

messages = []
encoding = "utf-8"

communicators = []

def id_generator():
    n = 0
    while True:
        yield n
        n += 1

id_gen = id_generator()

def always_listen(server_s):
    client_socket, client_address = server_s.accept()
    client_ip, client_port  = client_socket.getsockname())
    communicators.append(Communicator(client_socket, lock, client_ip, client_port))

listener_t = threading.Thread(target=always_listen, args=(server_s,))
listener_t.start()

"""
counter = 0
while counter < 10:
    counter += 1
    
    client_socket, client_address = server_socket.accept()
    
    data = client_socket.recv(1024).decode(encoding)
    
    if data == "get-messages":
        message = "\n".join(messages)
        client_socket.sendall(message.encode(encoding))
    else:
        messages.append(data)
    
    client_socket.close()

server_socket.close()
"""