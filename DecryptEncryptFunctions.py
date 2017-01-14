def powUpInModolu(a, b ,modul):
        nowNumber = 1
        for x in xrange(0,b):
                nowNumber = nowNumber * a
                if(nowNumber >= modul):
                        nowNumber = nowNumber - (nowNumber - (nowNumber % modul))
        return nowNumber

def encryptMessage(message, thisPrivateD, thisN, outPublicE, outN):
        newBlock = powUpInModolu(message, thisPrivateD, thisN)
        encryptedBlock = powUpInModolu(newBlock, outPublicE, outN)
        return encryptedBlock

def decryptMessage(enMessage, thisPrivateD, thisN, outPublicE, outN):
        newBlock = powUpInModolu(enMessage, thisPrivateD, thisN)
        decryptedBlock = powUpInModolu(newBlock, outPublicE, outN)
        return decryptedBlock

enM = encryptMessage(31, 55, 204, 7, 143)
deM = decryptMessage(enM, 103, 143, 7, 204)
print(enM)
print(deM)



