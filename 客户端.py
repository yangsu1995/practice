import socket, threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('UTF-8'))
for data in[b'nick',b'jordan',b'salah',b'lukaku']:
    s.send(data)
    print(s.recv(1024).decode('UTF-8'))
s.send(b'exit')
s.close()
