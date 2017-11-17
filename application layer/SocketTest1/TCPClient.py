from socket import *
serverName = 'xxxx.xxxx.xxx.xxxx'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input()
sentence = sentence.encode('utf-8')
clientSocket.send(sentence)
modifySentence = clientSocket.recv(1024)
print(modifySentence)
