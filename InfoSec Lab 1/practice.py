from socket import*

serPort=12000
serSocket=socket(AF_INET,SOCK_STREAM)
serSocket.bind(('',serPort))
serSocket.listen(1)

print("The server is ready to receive")

conSocket, addr=serSocket.accept()

print(addr)
file =open()
while True:
    data=conSocket.recv(1024)
    if not data:
        break
    file.write(data)

file.close()
conSocket.close()
serSocket.close()
