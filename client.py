import socket

# Example of setting up a socket connection to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8000))

file_request = "data.7z"
chunk_size = 4098
client_socket.send(file_request.encode())
client_socket.send(str(chunk_size).encode())

with open(file_request, 'wb') as file:
    while True:
        data = client_socket.recv(chunk_size)
        if not data:
            break
        file.write(data)
print(f"File {file_request} received successfully.")