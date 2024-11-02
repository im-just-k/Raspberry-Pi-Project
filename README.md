# Setting up the Server
Documentation for "server2.py"
## Features
- **Multi-client Support:** Capable of handling multiple client connections concurrently
- **User-friendly Disconnection:** Manages client disconnections without crashing
- **Server-side Messaging:** Server can send messages to all connected clients



## Code Overview

### Getting Started

#### **1. Imports:** 
The code imports the `socket` module for network communication and the the `threading` module for handling multiple clients.

#### **2. Server Configuration:**
    HOST = '0.0.0.0'
    PORT = 8000
- `Host`: Set to `0.0.0.0` to accept configurations from any IP address
- `Port`: The port number (8000) on which the server will listen for incoming connections

#### **3. Global Variables:**
    clients = []
- `clients`: A list that holds the socket connections of all connected clients

### Functions

1. `broadcast(message, ender_socket=None)`
#### **Purpose:** 
Sends a message to all connected clients except the one that sent it.

#### **Parameters:**
- `message`: The message to be sent.
- `sender_socket`: The socket of the client that sent the original message.

#### **Functionality**
Iterates through the clients and sends the message, removing clients that cannot be reached.

###
2. `handle_client(client_socket, address)`

#### **Purpose:** 
Manages the interaction with each connected client.

#### **Parameters:**
- `client_socket`: The socket of the connected client.
- `address`: Address of the connected client

#### **Functionality:**
Receives messages in a loop, broadcasts them to other clients, and handles any disconnections.

3. `server_send()`

#### **Purpose:** 
Allows the server operator to send messages to all clients.

#### **Functionality:**
Prompts the operator for input and broadcasts any entered message. Exits the server if the input is "exit".

4. `start_server()`

#### **Purpose:** 
Initializes and starts the server.

#### **Functionality:**
- Creates a TCP/IP socket.
- Binds to the specified host and port.
- Listens for incoming connections.
- Starts a thread for server-side messaging.
- Accepts and handles new client connections.

# Connecting Clients to the Server
Documentation for "client.py"

## Features
- **Client to Client Communication:** Capable of communicating with one or more clients

- **User-friendly disconnection message:** Allows users to close the connection by simply typing "exit". This ensures the socket is properly closed and prevents memory leaks

- **Dynamic Connection Handling:** The code includes error handling for connection attempts. If the connection to the server fails, it informs the user without crashing the program.

## Code Overview

### Getting Started

#### **1. Imports:** 
The code imports the `socket` module for network communication (as mentioned in the server-side documentation) and the `threading` module for allowing the program to create and manage threads, enabling concurrent operations.

#### **2. Configuration:**
    SERVER_IP = '192.168.1.3'  # Replace with actual server IP
    SERVER_PORT = 8080
- **SERVER_IP:** The IP address of the server to which the client will connect. Replace this with the actual server IP.
- **SERVER_PORT:** The port number on which the server is listening for connections.

#### **3. Receiving Messages:**
    def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print("Message received:", message)  # Debug: Print received messages
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break
**receive_messages(client_socket):** This function runs in a separate thread and is responsible for receiving messages from the server.

- **Loop:** Continuously listens for incoming messages.
- recv(1024): Receives up to 1024 bytes from the socket.
- **decode('utf-8'):** Converts the received bytes into a UTF-8 string.
- **Error Handling:** If there is an error (e.g., disconnection), it prints a message, closes the socket, and exits the loop.

#### **4. Client Setup and Main Logic:**
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

**start_client():** Initalizes client connection to the server.

- **Socket Creation:** A new TCP (Transmission Control Protocol) pocket is created using `socket.AF_INET` and `socket.SOCK_STREAM`
- **Connecting:** Attempts to connect to the specified server ID and port. If it is successful, it notifies the user. If it is unsuccessful, it catches the exception and prints the error message to the user.
- **Threading:** Starts a new thread to run the `receive_message()` function, allowing it to listen for incoming messages while the user can input messages.
- **User Input:** Enters a loop where it prompts the user to type messages. If the user types "exit", the connection is closed and the loop breaks. Otherwise, the message is sent to the server after encoding it as UTF-8.

#### **5. Main Execution:**
    if __name__ == "__main__":
        start_client()
This block checks if the script is being run directly (not imported as a module) and calls the `start_client()` function to initiate the client.

# Conclusion
This TCP client-server implementation provides a simple and effective way to for multiple clients to communicate with a server. It also exemplifies how computer networks operate on a base level and implies how they can be scaled up to serve a variety of needs. 


## Usage
- Open the "Terminal" application on your Ubuntu desktop and provide the computer with access to the correct .py file to intialize the server/connect the client to the server
- The Server and clients can now send and receive messages from each other over the computer network. You an test this by entering any message into the terminal and checking whether the message appears on the other computers
- Computers can now use the ping command to send queries to each other now
