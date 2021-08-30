import socket
#importing socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #here we using TCP protocol so we go with socket.SOCK_STREAM
#getting hostname

host = socket.gethostname()
#port listening

port = 443 # is my port number which data will be share via this port
#binding into socket

serversocket.blind((host,port))#replace host with your IP addr

#listener for Tcp client

serversocket.listen(2)#how many you wanna add this is number of client connect in your server

while True:
    #establishing connection
    clientsocket,address = serversocket.accept()
    print("connection recieved!! succesfully from %s "%str(address))#msg for server after connection details of the client
    
    message = 'Thank you for your connection'+"\r\n"
    
    clientsocket.send(message.encode('ascii')) #client to connection message
    #closing client socket

    clientsocket.close()
