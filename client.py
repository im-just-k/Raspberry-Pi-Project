# View the README.md file to see my own documentation

import socket
import threading

# Server IP and Port (make sure to replace with actual IP of the server)
SERVER_IP = '192.168.1.3'  # Replace with actual server IP
SERVER_PORT = 8000

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print("Message received:", message)  # Debug: Print received messages
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

# Set up the client
def start_client():
    print("Starting client...")  # Debug: Starting message
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("Connected to the server.")  # Debug: Connection success
    except Exception as e:
        print(f"Could not connect to server: {e}")  # Debug: Connection error
        return

    print("Type your messages below:")  # Debug: Ready to send messages

    # Start a thread to listen for messages
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("Closing connection...")
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
