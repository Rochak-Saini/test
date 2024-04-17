import socket
import datetime
import time
import threading

def send_local_time_to_master(master_host, master_port, production_line):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((master_host, master_port))
        
        while True:
            local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            client_socket.sendall(local_time.encode())
            
            print("Local time sent to master clock from production line at", production_line, ":", local_time)
            
            time.sleep(5)
    except Exception as e:
        print("Error:", e)
    finally:
        client_socket.close()

def main():
    master_host = '127.0.0.1'
    master_port = 8080
    
    production_lines = ['KMC', 'MIT', 'TAPMI', 'SOLS']
    
    for line in production_lines:
        threading.Thread(target=send_local_time_to_master, args=(master_host, master_port, line)).start()

if __name__ == "__main__":
    main()
