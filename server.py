import socket 
import sys

def decompress(data):
    return data # Implement your decompression algorithm here # Example using zlib: import zlib decompressed_data = zlib.decompress(data).decode('utf-8') return decompressed_data

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
            f.write(decompressed_data.decode('utf-8'))
        print("File decompressed and saved as received_file.txt")

        client_socket.close()
        server_socket.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__": 
    host = '127.0.0.1' 
    port = 12345
    file_path = "test_file.txt" # Replace with your file
    run_server(host, port)# Localhost port = 12345 run_server(host, port)