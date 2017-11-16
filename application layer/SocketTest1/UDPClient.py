from socket import *
serverName = 'xxxx.xxxx.xxxx.xxxx'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'hello'
message = message.encode('utf-8')#将字符串转为二进制串
#clientSocket.sendmsg(message, (serverName, serverPort))
clientSocket.sendto(message, (serverName, serverPort))
modifyMessage, sercerAddress = clientSocket.recvfrom(2048)
print(str(modifyMessage) + "    " + str(sercerAddress))
clientSocket.close();
