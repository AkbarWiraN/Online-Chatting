import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\n{message}")
            print("Type your message: ", end="", flush=True)
        except ConnectionResetError:
            break
    sock.close()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('167.71.214.226', 5555)) 

username = input("Enter your username: ")
client.send(username.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.daemon = True 
receive_thread.start()


while True:
    message = input("Type your message: ")
    client.send(message.encode('utf-8'))
