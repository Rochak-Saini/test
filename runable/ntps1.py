import socket
import time

HOST = 'localhost'  # Replace with actual server IP if needed
PORT = 65432        # Choose an unused port

def handle_client(conn):
  print("Connected by", conn.getpeername())
  server_time = time.time()
  conn.sendall(str(server_time).encode())
  conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  while True:
    conn, addr = s.accept()
    handle_client(conn)

print("Server stopped")
