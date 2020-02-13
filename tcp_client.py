# RC
# tcp_client.py
# using Python3
# 10-27-16

from socket import *
import sys  #for exit

# set server name: loop back
# server_name = '127.0.0.1'
server_port = 13000

while 1:
    choice = input("Enter L for Loan Calculation or X to quit: ")
    if choice == 'L':

        # create CLIENT SOCKET (TCP)
        try:
            client_socket = socket(AF_INET, SOCK_STREAM)
        except socket.error as msg:
            print("Unable to create socket. Error code: " + str(msg[0]) + " , Error message: " + msg[1])
            sys.exit()
        print("client socket created")

        # USER INPUT
        while(1):           
            server_name = input("Please enter hostname/IP: ")
            try:
                # CONVERT a name address to IP
                server_address = gethostbyname(server_name)
                break
            except gaierror as msg:
                print("bad address")

        while(1):
            the_loan = input("Enter loan amount: ")
            if the_loan.isdigit():
                break
        while(1):
            try:
                the_percent = input("Enter interest rate as a percentage (e.g., 5% = 5): ")
                the_percent = float(the_percent)
                break
            except ValueError as this:
                print("that's not a number!")
        while(1):
            the_period = input("Enter loan period: ")
            if the_period.isdigit():
                break

        # CONNECT TO SERVER
        client_socket.connect((server_address, server_port))

        # The stars are delimiters and separate the fused variables
        msg = the_loan + '*' + str(the_percent) + '*' + the_period
        
        # SEND DATA
        client_socket.send(msg.encode('utf-8'))

        # RECEIVE DATA from SERVER
        msg2 = client_socket.recv(2048)

        # DECODE back to utf-8 string type from bytecode
        msg2 = msg2.decode('utf-8')

        # SPLIT the string into the separate variables
        message_list = msg2.split('*')

        # ASSIGN variables by indexing the message list
        mth, tot = message_list
        mth = float(mth)
        tot = float(tot)

        # PRINT LOAN DETAILS
        print("Montly Payment: $%.2f" % mth)
        print("Total Payments: $%.2f" % tot + "\n")
        client_socket.close()

    if choice == 'X':
        print("Goodbye!")
        client_socket.close()
        break
