#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    serverSocket.bind(("", port))
    serverSocket.listen(2)
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024) #Fill in start    #Fill in end
            filename = message.split()[1]
            #print('Server received request for file: ' + filename.decode('ascii'))
            f = open(filename[1:])
            outputdata = f.read()#Fill in start     #Fill in end

            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send(bytes("HTTP/1.1 200 OK\n"
                            + "Content-Type: text/html\n"
                            + "\n", 'ascii'))
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            print('404: File not found')
            #Fill in start
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found\n"
                            + "Content-Type: text/html\n"
                            + "\n", 'ascii'))
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
