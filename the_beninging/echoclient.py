import socket

#handle ConnectionRefusedError

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 22222))
    
    user_input = bytes(input("SENDIE: "), "utf-8")

    s.sendall(user_input)
    data = s.recv(1024).decode("utf-8")
    if data == "gtfo":
        print(":(")

print(f"Received {data}")
