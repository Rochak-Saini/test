import socket
import time

HOST = 'localhost'  # Replace with server IP
PORT = 65432        # Same port as server

def get_synchronized_time():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Send request (empty message)
    s.sendall(b'')
    
    # Record send time
    send_time = time.time()
    
    # Receive server time
    server_time = float(s.recv(1024).decode())
    
    # Record receive time
    receive_time = time.time()
    
    # Calculate process delay
    process_delay = (receive_time - send_time) / 2
    
    # Calculate synchronized client time
    synchronized_time = server_time + process_delay
    
    # Calculate synchronization error
    synchronization_error = synchronized_time - receive_time
    
    print("Actual Clock Time:", time.ctime())
    print("Process Delay Latency:", process_delay, "seconds")
    print("Synchronized Client Time:", time.ctime(synchronized_time))
    print("Synchronization Error:", synchronization_error, "seconds")
    return synchronized_time

if __name__ == "__main__":
  get_synchronized_time()
