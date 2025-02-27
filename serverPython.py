import socket

# Define the host and port to listen on
host = '192.168.17.128'  # Change this to your desired host
port = 8484  # Change this to your desired port

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
sock.bind((host, port))

# Listen for incoming connections
sock.listen(1)

print("Server is listening on {}:{}".format(host, port))

# Accept a connection from a client
client_socket, client_address = sock.accept()
print("Connected to {}:{}".format(client_address[0], client_address[1]))

# Receive data from the client
while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print("Received data: {}".format(data))

    # Echo the received data back to the client
    client_socket.sendall(data.encode('utf-8'))

# Close the client socket
client_socket.close()

# Close the server socket
sock.close()
