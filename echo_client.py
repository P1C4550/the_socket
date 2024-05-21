import socket, os

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 22222))
        
        user_input = input("SENDIE: ").encode("utf-8")
        
        s.sendall(user_input)
        if user_input.decode("utf-8") == "get-messages":
            data = s.recv(1024).decode("utf-8")
            os.system("cls")
            print(data)
