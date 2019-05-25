import socket

s = socket.socket()

host = socket.gethostname()
s.bind((host, 12345))
s.listen(5)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    while data:
        print(data)
        data = conn.recv(1024)
    print("Data Received")
    conn.close()
    break