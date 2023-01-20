#!/usr/bin/env python3
import socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",12345))
data = s.recv(1024).decode()
print(data)
mes=input("Vvedi zapros:")
mes=mes.split()
if mes[0] == "list":
 s.send(b"list\n")
 buff=s.recv(1024)
 print(buff.decode().split())
elif mes[0] == "get":
 s.send(b"get\n")
 data=s.recv(1024)
 print(data)
 mes1=input("Vvedite kluch:")
 s.send(mes1.split()[0].encode()+b"\n")
 buff=s.recv(1024)
 print("Polucheno value:",buff.decode())
elif mes[0] == "put":
 s.send(b"set\n")
 data=s.recv(1024).decode()
 print(data)
 mes1=input("Vvedite key and value:")
 s.send(mes1.split()[0].encode()+b"\n")
 datass=s.recv(1024).decode()
 print(datass)
 s.send(mes1.split()[1].encode()+b"\n")
 datass1=s.recv(1024).decode()
 print(datass1)
else:
 s.send("0".encode())
 print("Neverniy zapros,poprobuy snova")
