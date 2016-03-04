import socket
req = raw_input("Input your message:")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0', 2222))
s.send(req)
resp = s.recv(1024)
print(resp)
s.close()
