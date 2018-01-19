import socket
import threading
import time
from appJar import gui


def mainfunc():
    


    tLock = threading.Lock()
    shutdown = False

    def receving(name, sock):
        while not shutdown:
            try:
                tLock.acquire()
                while True:
                    data, addr = sock.recvfrom(1024)
                    print str(data)

            except:
                     pass
            finally:
                    tLock.release()
    host = "127.0.0.1"
    port = 0
    server =("127.0.0.1", 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    s.setblocking(0)

    rT = threading.Thread(target=receving, args=("RecvThread", s))
    rT.start()

    alias = app.getEntry('Name')
    message = alias + app.getEntry('e1')
    
        
    while message != "q":
        if message !='':
             

            s.sendto(alias + ": " + message, server)
            tLock.acquire()
            app.setFocus('e1')
            message = raw_input(">>>")+ alias
            tLock.release() 
            time.sleep(0.2)

    shutdown = True
    rT.join()
    s.close()

app = gui()
app.setGeometry('250','400')
app.addLabel('t1','Client')
app.addListBox('list',[])
app.setLabelBg('t1', 'green')
app.addEntry('e1')

host = "127.0.0.1"
port = 0
server = ("127.0.0.1", 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
message = app.getEntry('e1')

def send(button):
    if button == "Send":
        message = app.getEntry('e1')
        s.sendto(message, server)
        app.addListItem('list',message)
        
        


app.addButton('Send',send)


def looprecv(name, sock):

    while True:
        
        host = "127.0.0.1"
        port = 0
        server = ("127.0.0.1", 5000)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host, port))
        message = app.getEntry('e1')


        data, addr = sock.recvfrom(1024)
        print data



def connect(con):
    if con == "Connect":
        app.registerEvent(looprecv)
        mainfunc()
app.addButton('Connect', connect)
app.addLabelEntry('Name')

app.go()
