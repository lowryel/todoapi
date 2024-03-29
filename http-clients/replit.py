import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(self.client_address[0])
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__ == '__main__':
    HOST,POTRT = 'localhost', 9999
    with socketserver.TCPServer((HOST, POTRT), MyTCPHandler) as server:
        server.serve_forever()
