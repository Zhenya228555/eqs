import socket 
# import pygame

desoll=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
desoll.bind(("localhost",1337))
desoll.setblocking(False)
desoll.listen(5)
plaers = {}
id = 1
print("working")
clients = []
while True:
    try:
        connect, ip = desoll.accept()
        connect.setblocking(False)
#     print("dlabla", ip)
        plaers[connect] = {
            "id":id,
            "x":0,
            "y":0,
            "radius":40,
            "name": None
        }
        connect.send(f"{plaers["id"]},{plaers["x"]},{plaers["y"]},{plaers["radius"]}{plaers["name"]}".encode())
        id += 1
    except:
        pass 
