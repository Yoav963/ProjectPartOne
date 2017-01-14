from socket import *
serverPort = 12005
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready'
connectionSocket, addr = serverSocket.accept()
connectionSocket.recv(86)
connectionSocket.send('r')
print 'message recived'
raw_input('Enter key to close server...')
connectionSocket.close()
