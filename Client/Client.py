import socket

class Client:
    def __init__(self, host='localhost', port=12345):
        self.Host = host
        self.Port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.Host, self.Port))
            print(f"Connected to server at {self.Host}:{self.Port}")
        except ConnectionRefusedError:
            print("Connection failed. Is the server running?")
            return False
        return True

    def send_message(self, message):
        self.client_socket.sendall(message.encode())
        data = self.client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

    def close(self):
        self.client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    client = Client()
    if client.connect():
        client.send_message("Molweni, server!")
        client.close()
