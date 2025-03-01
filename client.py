import socket
import sys

def compress(data):
    return data # Implement your compression algorithm here # Example using zlib: import zlib compressed_data = zlib.compress(data.encode('utf-8')) return compressed_data

def run_client(host, port, file_path): 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            with open(file_path, "r") as f:
                file_content = f.read()

                compressed_content = compress(file_content)
                print("File compressed.")

                client_socket.sendall(compressed_content.encode('utf-8'))
                print("Data sent.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    host = '127.0.0.1' # Localhost
    port = 12345
    file_path = "testfile.txt" # Replace with your file
    run_client(host, port, file_path)