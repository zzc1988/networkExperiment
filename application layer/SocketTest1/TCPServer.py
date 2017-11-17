from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
     connectionSock, addr = serverSocket.accept()
     sentence = connectionSock.recv(1024)
     print(str(sentence) + "   " + str(addr))
     sentence = sentence.upper()
     connectionSock.send(sentence)
     connectionSock.close()
