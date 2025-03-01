# 2.2.3 Challenge: Compressed Data Transmitter
Challenge developed by AI based on a prompt containing all of the essential understanding behind 2.2.3

# Solve

1. Fix the code to the correct format. There is code before the actual code block and indents that were not correct from the beginning.
1. Test both programs with a simple text file. Ensure the text file is in the same dir as the rest of the files.
1. Both client and server can be ran from the same computer. It is not necessary to use two systems to test the code out. Once it is achieved in one system a second system can be involved.

# Objective: Create a Python application that sends a text file over a network using sockets, compressing the data before transmission and decompressing it upon reception.

## Requirements:

Compression:
Implement a simple compression algorithm of your choice. (Suggestions: Run-length encoding (RLE), simple substitution, or even using the zlib library).
Compress the text file's content before sending it.
Sockets:
Use Python's socket library to establish a client-server connection.
The client should read a text file, compress it, and send it to the server.
The server should receive the compressed data, decompress it, and save it to a new file.
Error Handling:
Include basic error handling for socket connections and file operations.
Clear Output:
Print messages to the console indicating the progress of the application (e.g., "File compressed," "Data sent," "Data received," "File decompressed").
Code Examples and Guidance:

1. Server-Side (server.py):

Python

import socket
import sys

def decompress(data):
    # Implement your decompression algorithm here
    # Example using zlib:
    import zlib
    decompressed_data = zlib.decompress(data).decode('utf-8')
    return decompressed_data

def run_server(host, port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        received_data = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            received_data += chunk

        print("Data received.")
        decompressed_data = decompress(received_data)

        with open("received_file.txt", "w") as f:
            f.write(decompressed_data)
        print("File decompressed and saved as received_file.txt")

        client_socket.close()
        server_socket.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = '127.0.0.1'  # Localhost
    port = 12345
    run_server(host, port)
2. Client-Side (client.py):

Python

import socket
import sys

def compress(data):
    # Implement your compression algorithm here
    # Example using zlib:
    import zlib
    compressed_data = zlib.compress(data.encode('utf-8'))
    return compressed_data

def run_client(host, port, file_path):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        with open(file_path, "r") as f:
            file_content = f.read()

        compressed_content = compress(file_content)
        print("File compressed.")

        client_socket.sendall(compressed_content)
        print("Data sent.")

        client_socket.close()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = '127.0.0.1'  # Localhost
    port = 12345
    file_path = "test_file.txt"  # Replace with your file

    #Create a test file.
    with open(file_path, "w") as f:
        f.write("This is a test file. This file will be compressed and sent over the network.")

    run_client(host, port, file_path)
Key Concepts to Emphasize:

Socket Creation: socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Binding and Listening (Server): bind(), listen()
Connecting (Client): connect()
Sending Data: sendall()
Receiving Data: recv()
Closing Sockets: close()
Compression/Decompression: Implementing a simple algorithm or using zlib.
Error handling: using try and except blocks.
Enhancements (Optional):

Implement a more efficient compression algorithm.
Add a header to the transmitted data to indicate the length of the compressed data.
Add a simple GUI using Tkinter or PyQt.
Add a progress bar.
Add the ability to send multiple files.
Add the ability to send other file types.

Original Prompt:
Create a challenge to be written in Python using sockets by a HIgh school student that has a basic understanding of network fundamentals such as finding an IP address, an understanding of transmission using packets and protocols, and basic concept behind data compression that challenges them to create an app that transmits data through the network as a compressed algorithm of their choice. Include code examples to fill in information about the sockets and how to use them.
