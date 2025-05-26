


import socket


class Server:
    def __init__(self, host="localhost", port=12345) -> None:
    
        self.Host = host
        self.Port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.Host, self.Port))
        self.server_socket.listen()
        print(f"Server listening on {self.Host}:{self.Port}")

        try:
            while True:
                conn, addr = self.server_socket.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024).decode("utf-8")
                        # if not data:
                        #     break
                        # message = data.decode()
                        print(f"Received from client: {data}")

                        conn.sendall(data)  # Echo back
        except KeyboardInterrupt:
            print("\nServer shutting down.")
        finally:
            self.server_socket.close()

if __name__ == "__main__":
    server = Server(host="localhost", port=12345)
    server.start()