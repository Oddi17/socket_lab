#!/usr/bin/env python3
import socket,time,json,os
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("localhost",12345))
s.listen(2)
database = {}
cmd="0"
#print(cmd)
if os.path.isfile("data.json"):
    database=json.load(open("data.json","r"))
while 1:
   print("Waiting connect...")
   s2,remote_addr=s.accept()
   print("User is connected")
   mes="Vvedite comandu:list,get or put".encode()
   datas2=s2.send(mes)
   for e in range(10):
        cmd = s2.recv(1024)
        if cmd == b"list\n":
            print("making command: %s for list of keys"%cmd.decode().replace('\n',''))
            for k in database:
                s2.send(k.encode())
        elif cmd == b"get\n":
            print("making coomand: %s for get value"%cmd.decode().replace('\n',''))
            s2.send("key name required".encode())
            data1=s2.recv(1024)
            k=data1.decode()
            s2.send(database[k].encode())
        elif cmd == b"set\n":
            print("making command: %s for put keys and value"%cmd.decode().replace('\n',''))
            s2.send("key name and value required!".encode())
            data2=s2.recv(1024)
            k = data2.decode()
            s2.send(("Key:%s"%k.rstrip()).encode())
            data3=s2.recv(1024)
            v = data3.decode()
            s2.send(("Value:%s"%v.rstrip()).encode())
            database [k]=v
            json.dump(database,open("data.json","w"))
        elif cmd.rstrip().decode() == "0":
           print("ERROR!User was disconnected")
        else: 
          break
   
