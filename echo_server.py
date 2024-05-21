import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 22222))
server_socket.listen(10)
print("Server listen")

messages = []

counter = 0
while counter < 10:
    counter += 1
    
    client_socket, client_address = server_socket.accept()
    
    data = client_socket.recv(1024).decode("utf-8")
    
    if data == "get-messages":
        message = "\n".join(messages)
        client_socket.sendall(message.encode("utf-8"))
    else:
        messages.append(data)
    
    client_socket.close()

server_socket.close()
