import socket
import threading

# Create a socket object using the TCP/IP protocol
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8000
queue_size = 5
server_socket.bind(('192.168.1.4', port))
server_socket.listen(queue_size)

print(f"Server listening on port { port }... with queue size { queue_size }")

path = "C:\\Users\\_\\Desktop\\"


# Logic for handling each client connection
def handle_client(client_conn, client_addr):
    chunk_size = 1024

    # See what file and chunk size
    file_request = client_conn.recv(chunk_size).decode()
    chunk_size = client_conn.recv(chunk_size).decode()
    chunk_size = int(chunk_size)
    
    print(f"File: { file_request }, with chunk size: { chunk_size }")

    try:
        with open(path + file_request, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                
                client_conn.sendall(chunk)

    except FileNotFoundError:
        client_conn.send(b"File not found.")

    client_conn.close()

    pass

while True:
    client_conn, client_addr = server_socket.accept()
    print(f"Connected to {client_addr}")

    thread = threading.Thread(target=handle_client, args=(client_conn, client_addr))
    thread.start()
