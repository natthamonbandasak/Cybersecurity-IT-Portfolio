# Establish a low-level TCP socket connection and send a raw HTTP GET request

import socket

# Define target host and port
host = 'data.pr4e.org'
port = 80
target_url = 'http://data.pr4e.org/intro-short.txt'

try:
    # Create an IPv4, TCP socket and establish connection
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, port))
    
    # Formulate and send the raw HTTP GET request
    cmd = f'GET {target_url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
    print(f"--- Successfully connected to {host} ---\n")
    
    # Receive and display the data in chunks of 512 bytes
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
        
except socket.error as e:
    print(f"Network Error: Could not connect to the server. Details: {e}")
    
finally:
    # Ensure the socket is securely closed to free up system resources
    mysock.close()
    print("\n\n--- Connection Closed ---")
