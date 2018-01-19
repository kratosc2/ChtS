import socket
import time
from appJar import gui

app = gui()
app.setFont(10)
app.addLabel('title2', 'Server')
app.setLabelBg('title2', 'blue')

def mainpc():
    green = '\033[92m'
    host = "127.0.0.1"
    port = 5000

    clients = []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    s.setblocking(0)
    quitting = False

    app.addLabel('label', 'Connected')
    
    
    
    while not quitting:
        try:
            data, addr = s.recvfrom(1024)
            if "Quit" in str(data):
                   quitting = True
            if addr not in clients:
                    clients.append(addr)

            app.addListItem('list', (str(data)))
            for client in clients:
                 s.sendto(data, client)
                 
        except:
            
            pass
    s.close()

def press(button):
    if button == "Cancel":       
        mainpc()
    else:
        app.stop()

app.addListBox('list', [''])
app.addButtons(["Cancel","OK"], press, )
app.go()

