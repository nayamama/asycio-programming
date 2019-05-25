import socket

sock = socket.socket()

host = socket.gethostname()
sock.connect((host, 12345))
sock.setblocking(0) # Now setting to non-blocking mode

data = b"Foo Bar" * 10 * 1024
assert sock.send(data)
print("Data sent")