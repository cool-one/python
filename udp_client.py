# RC
# UDPClient.py
# using Python3
# client side app
# 10-27-16
from socket import *
import array
import sys
import time
# port of server
serverPort = 13000

# create a UDP socket
try:
    client_socket = socket(AF_INET, SOCK_DGRAM)
except socket.error as msg:
    print("failed to create socket.  Error code: " + str(msg[0]) + 
    'error message: ' + msg[1])
    sys.exit();
print("UDP socket created\n")

while 1:    
    choice = input("Enter L for Loan Calculation or X to quit: ")

    if choice == 'L':

        # INPUT SERVER NAME
        while(1):           
            server_name = input("Please enter hostname/IP: ")
            try:
                # CONVERT a name address to IP
                sAddress = gethostbyname(server_name)
                break
            except gaierror as msg:
                print("bad address")
        # INPUT LOAN AMOUNT
        while(1):
            the_loan = input("Enter loan amount: ")
            if the_loan.isdigit():
                break
        # INPUT PERCENT
        while(1):
            try:
                the_percent = input("Enter interest rate as a percentage (e.g., 5% = 5): ")
                the_percent = float(the_percent)
                break
            except ValueError as this:
                print("that's not a number!")
        # INPUT PERIOD
        while(1):
            the_period = input("Enter loan period: ")
            if the_period.isdigit():
                break

        # The stars are delimiters and separate the fused variables
        the_data = the_loan + '*' + str(the_percent) + '*' + the_period

        # send the_data list to Server for processing
        client_socket.sendto(str(the_data).encode('utf-8'),(sAddress, serverPort))
        print("data sent to server for processing")

        # RECEIVE DATA
        msg2, server_address = client_socket.recvfrom(2048)
        print("received data from: " + str(server_address))
                
        # DECODE back to utf-8 string type from bytecode
        msg2 = msg2.decode('utf-8')

        # SPLIT the string into the separate variables
        msg2List = msg2.split('*')

        # ASSIGN variables by indexing the message list
        mth, tot = msg2List
        mth = float(mth)
        tot = float(tot)

        # PRINT LOAN DETAILS
        print("Montly Payment: $%.2f" % mth)
        print("Total Payments: $%.2f" % tot + "\n")

    if choice == 'X':
        client_socket.close()
        print("Goodbye!")
        break
