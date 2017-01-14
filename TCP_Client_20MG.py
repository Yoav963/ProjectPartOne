from socket import *
BlockSized = 86


serverName = raw_input('Server name:')
serverPort = raw_input('Server port:')
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


respond = clientSocket.recv(BlockSized)
print(powUpInModolu(2,3,5))



def powUpInModolu(a, b ,modul):
        nowNumber = 1
        for x in xrange(0,b):
                nowNumber = nowNumber * a
                if(nowNumber >= b):
                        nowNumber = nowNumber - b
        return nowNumber



