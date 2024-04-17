import socket
import datetime
import threading
import time

client_data = {}

def handle_client_connection(client_socket, client_address):
    try:
        while True:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            client_socket.sendall(current_time.encode())
            
            time.sleep(60)  
    except Exception as e:
        print("Error handling client connection:", e)
    finally:
        client_socket.close()

def main():
    server_host = '127.0.0.1'
    server_port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((server_host, server_port))
        
        server_socket.listen(5)
        print("Time server started on", server_host, "port", server_port)
        
        while True:
            client_socket, client_address = server_socket.accept()
            print("Connected to client:", client_address)
            
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, client_address))
            client_thread.start()
    except Exception as e:
        print("Error:", e)
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
