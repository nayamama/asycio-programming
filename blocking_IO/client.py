import socket

sock = socket.socket()

host = socket.gethostname()
sock.connect((host, 12345))

data = b"Foo " * 10 * 1024
assert sock.send(data)
print("Data sent")