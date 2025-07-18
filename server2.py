# View the README.md file to see my own documentation

import socket
import threading

# Server IP and Port
HOST = '0.0.0.0'
PORT = 8000

# List to hold connected clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message, sender_socket=None):
    for client in clients:
        # Send the message to all clients except the sender (if specified)
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# Handle each client connection
def handle_client(client_socket, address):
    print(f"New connection from {address}")
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if not message:
                print(f"Connection closed by {address}")
                break

            # Print the message on the server console and broadcast to others
            print(f"{address}: {message.decode('utf-8')}")
            broadcast(message, sender_socket=client_socket)
        except:
            # Handle client disconnection
            print(f"Connection error with {address}")
            break

    # Remove client from the list after disconnecting
    client_socket.close()
    clients.remove(client_socket)

# Function to handle server-side input and broadcast to all clients
def server_send():
    while True:
        message = input("Server: ")
        if message.lower() == 'exit':
            print("Server shutting down...")
            for client in clients:
                client.close()
            break
        broadcast(f"Server: {message}".encode('utf-8'))

# Set up the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    # Start a thread to allow server to send messages
    threading.Thread(target=server_send).start()

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    start_server()
