#підключеня модуля
import socket 
from threading import Thread
#дае змогу пидключеня клийента до сервера
desoll=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
desoll.bind(("localhost",1337))
desoll.setblocking(False)
desoll.listen(5)
plaers = {}
id = 1


def a():
    for connect in list(plaers):

        try:
            e=connect.recv(1024).decode()
            print(e)
        except:
            pass


#говорить шо вин працюе
print("working")
#список клийентиф
clients = []
#бескинечний цикел
while True:
    try:
        connect, ip = desoll.accept()
        connect.setblocking(False)
        plaers[connect] = {"id":id,"x":0,"y":0,"radius":40,"name": None}
        connect.send(f"{id},0,0,20".encode())
        id += 1
        
    except:
        pass 
