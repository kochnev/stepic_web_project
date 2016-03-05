import socket
import threading

class MyThread(threading.Thread):
    def __init__(self, channel, details):
        self.channel = channel
        self.details = details
        threading.Thread.__init__(self)
    
    def run(self):
        print("Recieved connection:" + self.details[0])
        data = self.channel.recv(1024)
        if data:
            if data != 'close':
                self.channel.send(data)
                print data       
        self.channel.close()
        print("Closed connection:" + self.details[0])
                       

#set server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)


while True:
    conn, addr = s.accept()
    MyThread(conn, addr).start()
    
    
