from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)#ipv4 UDP
serverSocket.bind('', serverPort)
print('the server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(str(message) + "    " + clientAddress)
    modifyMessage = message.upper()
    serverSocket.sendto(modifyMessage, modifyMessage)
