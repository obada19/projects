import socketserver
from socket import socket, SOCK_STREAM, AF_INET, SOL_SOCKET, SO_REUSEADDR


class Handler_TCPServer(socketserver.BaseRequestHandler):
    """
    The TCP Server class for demonstration.

    Note: We need to implement the Handle method to exchange data
    with TCP client.

    """

    def handle(self):
        # self.request - TCP socket connected to the client
        self.data = self.request.recv(1024).upper()
        print("{} sent:".format(self.client_address[0]).upper())
        print(self.data)

        # just send back ACK for data arrival confirmation
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Init the TCP server object, bind it to the localhost on 9999 port
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)


    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()