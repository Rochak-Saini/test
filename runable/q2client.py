import socket
import datetime
import time

def request_time_from_server(server_host, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        client_socket.connect((server_host, server_port))
        
        while True:
            client_socket.send(b'RequestTime')
            
            server_time_str = client_socket.recv(1024).decode()
            server_time = datetime.datetime.strptime(server_time_str, "%Y-%m-%d %H:%M:%S")
            
            adjust_local_clock(server_time)
            
            time.sleep(60) 
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

def adjust_local_clock(server_time):
    local_time = datetime.datetime.now()
    offset = server_time - local_time
    adjusted_time = local_time + offset
    print("Server time:", server_time)
    print("Local time:", local_time)
    print("Offset:", offset)
    print("Adjusted time:", adjusted_time)

def main():
    server_host = '127.0.0.1'
    server_port = 12345
    
    request_time_from_server(server_host, server_port)

if __name__ == "__main__":
    main()
