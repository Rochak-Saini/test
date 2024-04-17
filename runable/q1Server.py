import socket
import datetime
import threading

# Global variables
client_data = {}
master_host = '127.0.0.1'
master_port = 8080

# Function to handle client connections and synchronization
def handle_client_connection(client_socket, client_address):
    try:
        while True:
            # Receive clock time from the client
            clock_time_str = client_socket.recv(1024).decode()
            clock_time = datetime.datetime.strptime(clock_time_str, "%Y-%m-%d %H:%M:%S")
            
            # Update client data with received clock time
            client_data[client_address] = clock_time
            
            # Calculate average clock difference and synchronize clocks
            synchronize_clocks()
    except Exception as e:
        print("Error handling client connection:", e)
    finally:
        # Close the client socket connection
        client_socket.close()

# Function to calculate average clock difference and synchronize clocks
def synchronize_clocks():
    try:
        if len(client_data) > 0:
            # Calculate average clock difference
            total_difference = sum((datetime.datetime.now() - time).total_seconds() for time in client_data.values())
            average_difference = datetime.timedelta(seconds=total_difference / len(client_data))
            
            # Synchronize clocks
            for address, time in client_data.items():
                synchronized_time = time + average_difference
                print("Synchronized time for production line at", address, ":", synchronized_time)
        else:
            print("No production line data. Synchronization not applicable.")
    except Exception as e:
        print("Error synchronizing clocks:", e)

# Main function to initialize the master clock server
def main():
    # Setup master clock server socket
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Bind the socket to the host and port
        master_socket.bind((master_host, master_port))
        
        # Listen for incoming connections
        master_socket.listen(5)
        print("Master clock server started on", master_host, "port", master_port)
        
        while True:
            # Accept incoming connections from production line clocks
            client_socket, client_address = master_socket.accept()
            print("Connected to production line at:", client_address)
            
            # Start a new thread to handle the client connection
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, client_address))
            client_thread.start()
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the master socket when done
        master_socket.close()

# Entry point of the program
if __name__ == "__main__":
    main()
