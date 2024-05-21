import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 22222))
server_socket.listen(10)
print("Server listen")

counter = 0
while counter < 10:
    counter += 1
    
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} has connected")
    data = str(client_socket.recv(1024))
    print(f"data: {data}")
    client_socket.sendall(f"{data}".encode())
    client_socket.close()
    
    print("closed socket")

server_socket.close()
