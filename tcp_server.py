#RC
#using Python3
#TCPServer.py
#10-27-16

from socket import *
import sys  #for exit
serverPort = 13000

#functions for loan calculations-------------------------------------------------------------------------------------
def monthly(L, R, N):
    R = R/100
    MP = (L * R / (1 - (1/(1+R))**N))
    return MP

def total(MP, N):
    TP = (MP * N)
    return TP
#--------------------------------------------------------------------------------------------------------------------
#create a TCP server socket
try:
    serverSocket = socket(AF_INET,SOCK_STREAM)
except socket.error as msg:
    print("Unable to create socket. Error code: " + str(msg[0]) + " , Error message: " + msg[1])
    sys.exit() 
    
print("server socket created")

serverSocket.bind(('',serverPort))

#listens for knocks from clients, sets max # of queued connections to 1
serverSocket.listen(1)
print ('The server is listening')

while True:
    # Establishes new CONNECTION SOCKET (specific to a particular client)
    connectionSocket, addr = serverSocket.accept()
    print("client connected")

    # RECEIVE DATA from Client
    msg = connectionSocket.recv(2048)

    # DECODE back to utf-8 string type from bytecode
    msg = msg.decode('utf-8')

    # SPLIT the string into the separate variables
    msgList = msg.split('*')
    #~print(msg, msgList)

    # ASSIGN variables by indexing the message list
    Loan, Percent, Period = msgList

    # PROCESS DATA (variables are typecast from string-type to required types)
    mth = monthly(int(Loan), float(Percent), int(Period))
    tot = total(float(mth), int(Period))
    #~print("Sending:", mth, tot)

    # FORMAT DATA into string with delimiters
    msg2 = str(mth) + '*' + str(tot)

    # SEND DATA
    connectionSocket.send(msg2.encode('utf-8'))
       
    #could have receive client request to close
    #closes connectionSocket, but serverSocket stays open
    connectionSocket.close()
    print("client disconnected")
