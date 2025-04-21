grp.py

import socket
import threading

clients = []  # List to store client connections

# Send message to all clients
def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.lower() == "exit":
                break
            print(msg)
            broadcast(msg, sender=client)
        except:
            break

    client.close()
    clients.remove(client)
    print("A user disconnected.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 1234))
    server.listen()
    print("Group Chat Server started...")

    while True:
        client, addr = server.accept()
        print(f"New user connected from {addr}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()

if __name__ == "__main__":
    main()






#grp_client.py

import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 1234))
    print("Connected to the Group Chat!")

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == "exit":
            break
        client.send(msg.encode())

    client.close()
    print("You left the chat.")

if __name__ == "__main__":
    main()
