# RC
# using Python3
# udp_server.py
# Server side app
# 10-27-16
from socket import *
import sys
import time
server_port = 13000

# sets up a server socket of type UDP
try:
    server_socket = socket(AF_INET, SOCK_DGRAM)
except socket.error as msg:
    print("failed to create socket.  Error code: " + str(msg[0]) + 
    'error message: ' + msg[1])
    sys.exit()
print('socket successfully created!')
    
# bind the newly created UDP socket
try:
    server_socket.bind(('', server_port))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print ("The server is ready to receive")

#--------------------------------------------------------------------------------------------------------------------
# L = loan amount
# R = monthly interest rate
# N = number of payments
# MP = monthly payment, TP = total payment
def monthly(L, R, N):
    R = R/100
    MP = (L * R / (1 - (1/(1+R))**N))
    return MP

def total(MP, N):
    TP = (MP * N)
    return TP
#--------------------------------------------------------------------------------------------------------------------

# server socket continuously listening
while 1:
    
    # receive the "the_data" list, set client address as recvd from
    the_data, client_address = server_socket.recvfrom(2048)
    print("received data from: " + str(client_address))

    # DECODE back to utf-8 string type from bytecode
    the_data = the_data.decode('utf-8')

    # SPLIT the string into the separate variables
    data_list = the_data.split('*')

    # ASSIGN variables by indexing the message list
    loan, percent, period = data_list

    # PROCESS DATA (variables are typecast from string-type to required types)
    mth = monthly(int(loan), float(percent), int(period))
    tot = total(float(mth), int(period))

    # FORMAT DATA into string with delimiters
    msg2 = str(mth) + '*' + str(tot)

    # SEND DATA
    server_socket.sendto(msg2.encode('utf-8'), client_address)
    print("processed data sent back to client")
