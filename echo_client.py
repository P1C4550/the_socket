import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 22222))
    
    user_input = bytes(input("SENDIE: "), "utf-8")

    s.sendall(user_input)
    data = s.recv(1024).decode("utf-8")

print(f"Received {data}")
