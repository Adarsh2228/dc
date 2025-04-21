#user_a.py

import socket
import threading

def receive_messages(conn):
    while True:
        message = conn.recv(1024).decode()
        if message.lower() == "exit":
            print("\nUser B has left the chat.")
            break
        print(f"\nUser B: {message}\nYou: ", end='')

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(1)
    print("User A is waiting for connection...")
    conn, addr = server_socket.accept()
    print("User B connected!")

    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

    while True:
        message = input("You: ")
        conn.send(message.encode())
        if message.lower() == "exit":
            break

    conn.close()
    server_socket.close()
    print("Chat closed.")

if __name__ == "__main__":
    main()

# user_b.py

import socket
import threading

def receive_messages(sock):
    while True:
        message = sock.recv(1024).decode()
        if message.lower() == "exit":
            print("\nUser A has left the chat.")
            break
        print(f"\nUser A: {message}\nYou: ", end='')

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 1234))
    print("Connected to User A!")

    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    while True:
        message = input("You: ")
        sock.send(message.encode())
        if message.lower() == "exit":
            break

    sock.close()
    print("Chat closed.")

if __name__ == "__main__":
    main()
