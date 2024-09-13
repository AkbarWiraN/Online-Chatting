import socket
import threading
from datetime import datetime


def handle_client(client_socket, username):
    while True:
        try:
            
            message = client_socket.recv(1024).decode('utf-8', errors='replace')
            if not message:
                break
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            formatted_message = f"{timestamp} {username}: {message}"
            print(f"Sending message: {formatted_message}")
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(formatted_message.encode('utf-8'))
                    except BrokenPipeError:
                        print(f"Failed to send message to a disconnected client.")
                        clients.remove(client) 
        except (ConnectionResetError, ConnectionAbortedError):
            print(f"Connection with {username} lost.")
            continue
        except UnicodeDecodeError as e:
            print(f"Error decoding message from {username}: {e}")
            continue  

    client_socket.close()
    clients.remove(client_socket)
    print(f"Connection with {username} closed.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 5555))
server.listen(5)
print("Server listening on port 5555")

clients = []

while True:
    try:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        username = client_socket.recv(1024).decode('utf-8', errors='replace').strip()

        if not username:
            print(f"Invalid username from {addr}")
            client_socket.close()
            continue
        
        clients.append(client_socket)
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
        client_handler.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
        continue
    except Exception as e:
        print(f"Error accepting connection: {e}")
        continue

server.close()
