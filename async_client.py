import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, mess):
        self.message = mess
        threading.Thread.__init__(self)
    
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('0.0.0.0.', 2222))
        s.send(mess)
        resp = s.recv(1024)
        print(resp)
        s.close()
        
for i in xrange(10):
    mess = "Hello server:" +str(i)
    ClientThread(mess).start()



