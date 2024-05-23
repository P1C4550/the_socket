import socket, threading

class Communicator:
    def __init__(s, socket, lock, ip, port, id):
        s.socket = socket
        s.queue = []
        s.lock = lock
        s.ip = ip
        s.port = port
        
        s.data_size = 1024
        s.encoding = "utf-8"
        
        s.socket.settimeout(None)
        
        listener_t = threading.Thread(target=s.listen, args=())
        listener_t.start()
        
    def listen(s):
        data = s.socket.recv(s.data_size).decode(s.encoding)
        s.queue.append(data)
    
    def quit(s):
        pass