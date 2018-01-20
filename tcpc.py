import socket
import threading
import time
from appJar import gui


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
app.setEntryDefault('e1', '')

def send(button):
    if button == "Send":
        app.setEntryFg("e1",'green')
        message =(app.getEntry('Name') + ':' + app.getEntry('e1')  )
        s.sendto(message, server)
        app.clearEntry('e1')
        
        
app.addButton('Send',send)
app.addLabelEntry('Name')
app.setFocus('Name')
app.get

downloadCount = 0
green = '\033[92m'
def downloader():
    global downloadCount
    for i in range(20020):
        daa = s.recv(20)
        app.addListItem('list', daa)
        app.setListItemFg('list','daa','green')
        app.addListItem('list', "")
        time.sleep(1)

app.thread(downloader)




app.go()
