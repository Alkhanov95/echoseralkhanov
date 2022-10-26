import socket
import pickle

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

msg = conn.recv(1024)
print(msg)
conn.send(msg)

conn.close()
