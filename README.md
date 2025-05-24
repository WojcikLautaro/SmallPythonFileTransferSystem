# SmallPythonFileTransferSystem
This project demonstrates a barebones file transfer system using Python's built-in socket module. It consists of a TCP server that serves files from a predefined folder and a client that requests and downloads them.

##Overview
The server listens on a local IP and waits for incoming client connections.

The client connects to the server, requests a file by name, and downloads it in chunks.

Both server and client use a simple custom protocol: the client sends the file name and chunk size, then receives the file data.

##How to Run
Edit server.py to set the correct file path.

Then run: 
  python server.py

Make sure the client can reach the server at the given IP. In client.py, you can change:
  file_request = "data.7z"  # replace with the actual file you want

Then run: 
  python client.py

##Features
-Simple TCP socket communication.
-Multithreaded server to handle multiple clients.
-Custom chunk size for efficient large file transfer.

##Limitations
-No encryption or authentication.
-No error handling for bad file names on the client side.
-Only supports files in a hardcoded directory.
-File size or name is not validated—use at your own risk.
-Do not run the client and server on the same computer if you're testing file transfer to avoid overwriting the source file. :D
